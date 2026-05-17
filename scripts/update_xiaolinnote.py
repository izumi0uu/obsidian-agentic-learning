#!/usr/bin/env python3
"""Update xiaolinnote.com raw source notes in the Agentic Learning Obsidian vault.

Usage:
  python scripts/update_xiaolinnote.py
  python scripts/update_xiaolinnote.py --scope ai
  python scripts/update_xiaolinnote.py --dry-run

The script reads https://xiaolinnote.com/sitemap.xml, extracts page markdown, compares
body sha256 values with existing raw notes, and writes only new/changed pages.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urljoin, urlparse

try:
    import requests
    from bs4 import BeautifulSoup
    from markdownify import markdownify as md
except ModuleNotFoundError as exc:
    raise SystemExit(
        "Missing dependency. Install with: python -m pip install beautifulsoup4 markdownify lxml requests\n"
        f"Original error: {exc}"
    )

ROOT = Path(__file__).resolve().parents[1]
VAULT = ROOT / "agentic learning"
RAW_ROOT = VAULT / "raw" / "repos" / "xiaolinnote"
OUT = RAW_ROOT / "questions"
COLLECTION = RAW_ROOT / "xiaolinnote 面试题索引.md"
MANIFEST = RAW_ROOT / "crawl-manifest.json"
COLLECTION_LINK = "[[raw/repos/xiaolinnote/xiaolinnote 面试题索引]]"
BASE = "https://xiaolinnote.com"
SITEMAP = BASE + "/sitemap.xml"
UA = "Mozilla/5.0 (compatible; HermesAgent/1.0; xiaolinnote-wiki-updater)"
WIKI_LINK_RE = re.compile(r"\[\[[^\]]+\]\]")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Update xiaolinnote.com raw source notes in the Obsidian vault.")
    p.add_argument("--scope", choices=["all", "ai"], default="all", help="Crawl all sitemap URLs or only /ai/ URLs.")
    p.add_argument("--dry-run", action="store_true", help="Compute changes without writing files.")
    p.add_argument("--no-log", action="store_true", help="Do not append/update agentic learning/log.md.")
    p.add_argument("--timeout", type=int, default=40, help="HTTP timeout seconds per request.")
    return p.parse_args()


def fetch(session: requests.Session, url: str, timeout: int) -> str:
    r = session.get(url, timeout=timeout)
    r.raise_for_status()
    if not r.encoding or r.encoding.lower() == "iso-8859-1":
        r.encoding = r.apparent_encoding or "utf-8"
    return r.text


def safe_name(url: str) -> str:
    path = urlparse(url).path.strip("/") or "index"
    if path.endswith(".html"):
        path = path[:-5]
    path = path.replace("/", " - ")
    path = re.sub(r"[\\/:*?\"<>|]+", "-", path).strip(" .")
    return path or "index"


def safe_file_stem(text: str, max_len: int = 180) -> str:
    text = re.sub(r"[\\/:*?\"<>|]+", "-", text).strip(" .")
    text = re.sub(r"\s+", " ", text)
    return (text[:max_len].rstrip(" .") or "untitled")


def title_from_page_title(title: str) -> str:
    return re.sub(r"\s*\|\s*(小林coding|小林面试笔记).*$", "", title).strip()


def category_prefix(url: str) -> str:
    parts = [p for p in urlparse(url).path.strip("/").split("/") if p]
    if not parts:
        return "home"
    if parts[0] == "ai" and len(parts) > 1:
        return f"ai {parts[1]}"
    return parts[0]


def topic_for(url: str) -> list[str]:
    p = urlparse(url).path.strip("/").lower()
    topics = ["interview"]
    if p.startswith("ai/") or p == "ai":
        topics += ["ai", "llm"]
    if p.startswith("ai/agent"):
        topics += ["agent"]
    if p.startswith("ai/rag"):
        topics += ["rag"]
    if p.startswith("ai/tools"):
        topics += ["tools", "mcp"]
    if p.startswith("ai/lang"):
        topics += ["langchain"]
    if p.startswith("git"):
        topics += ["git"]
    if p.startswith("linux"):
        topics += ["linux"]
    if p.startswith("sql"):
        topics += ["database", "sql"]
    out: list[str] = []
    for t in topics:
        if t not in out:
            out.append(t)
    return out


def yaml_list(vals: list[str], indent: int = 2) -> str:
    if not vals:
        return "[]"
    return "\n" + "\n".join(" " * indent + "- " + json.dumps(v, ensure_ascii=False) for v in vals)


def clean_markdown(text: str) -> str:
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"(?m)^\s*Last updated:.*$", "", text)
    return text.strip()


def split_frontmatter(text: str) -> tuple[str, str]:
    m = re.match(r"^---\n(.*?)\n---\n\n?(.*)$", text, re.S)
    if not m:
        return "", text
    return m.group(1), m.group(2)


def frontmatter_sha(text: str) -> str | None:
    fm, _body = split_frontmatter(text)
    m = re.search(r"(?m)^sha256:\s*([0-9a-f]{64})\s*$", fm)
    return m.group(1) if m else None


def frontmatter_scalar(fm: str, key: str) -> str | None:
    m = re.search(rf"(?m)^{re.escape(key)}:\s*(.*?)\s*$", fm)
    if not m:
        return None
    value = m.group(1).strip()
    if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
        value = value[1:-1]
    return value or None


def frontmatter_related(fm: str) -> list[str]:
    m = re.search(r"(?m)^related:\s*\n((?:[ \t]+-\s+.*(?:\n|$))*)", fm)
    if not m:
        return []
    items: list[str] = []
    for line in m.group(1).splitlines():
        raw = re.sub(r"^\s+-\s+", "", line).strip()
        if not raw:
            continue
        try:
            parsed = json.loads(raw)
            if isinstance(parsed, str):
                raw = parsed
        except json.JSONDecodeError:
            raw = raw.strip("'\"")
        items.append(raw)
    return items


def dedupe(values: list[str]) -> list[str]:
    out: list[str] = []
    seen: set[str] = set()
    for value in values:
        if value and value not in seen:
            out.append(value)
            seen.add(value)
    return out


def extract_related_section(body: str) -> str | None:
    m = re.search(r"(?ms)^## 相关知识 wiki\s*\n\n.*?(?=^##\s+|\Z)", body)
    if not m:
        return None
    return m.group(0).strip()


def default_wiki_targets(url: str) -> list[str]:
    path = urlparse(url).path.strip("/").lower()
    if path.startswith("ai/llm"):
        return ["[[LLM]]", "[[LLM 主题]]"]
    if path.startswith("ai/agent"):
        return ["[[Agent]]", "[[LLM]]"]
    if path.startswith("ai/rag"):
        return ["[[RAG]]", "[[LLM]]"]
    if path.startswith("ai/tools"):
        return ["[[Tool Calling]]", "[[LLM]]"]
    if path.startswith("ai/lang"):
        return ["[[Agent Framework]]", "[[Tool Calling]]"]
    return []


def related_section_from_targets(targets: list[str]) -> str | None:
    if not targets:
        return None
    lines = ["## 相关知识 wiki", ""]
    lines.extend(f"- {target}" for target in targets)
    return "\n".join(lines)


def insert_related_section(body: str, section: str | None) -> str:
    if not section:
        return body
    if re.search(r"(?m)^## 相关知识 wiki\s*$", body):
        return body
    marker = "## 页面正文\n\n"
    if marker in body:
        return body.replace(marker, section.strip() + "\n\n" + marker, 1)
    return body.rstrip() + "\n\n" + section.strip() + "\n"


def build_frontmatter(
    page: dict,
    today: str,
    existing_text: str | None,
    related_targets: list[str],
) -> str:
    old_fm = split_frontmatter(existing_text)[0] if existing_text else ""
    created = frontmatter_scalar(old_fm, "created") or today
    related = dedupe([COLLECTION_LINK, "[[资料收集索引]]", *frontmatter_related(old_fm), *related_targets])
    fm = "---\n"
    fm += "type: source\nsource_type: web\nsite: xiaolinnote.com\n"
    fm += "topic:" + yaml_list(page["topics"]) + "\n"
    fm += "status: inbox\n"
    fm += f"created: {created}\nupdated: {today}\n"
    fm += "url: " + json.dumps(page["url"], ensure_ascii=False) + "\n"
    fm += "source: " + json.dumps(page["url"], ensure_ascii=False) + "\n"
    fm += f"last_checked: {today}\nfreshness: watch\nsha256: {page['sha256']}\n"
    fm += "related:" + yaml_list(related) + "\n"
    fm += "---\n\n"
    return fm


def compose_content(page: dict, today: str, existing_text: str | None) -> str:
    old_body = split_frontmatter(existing_text)[1] if existing_text else ""
    existing_section = extract_related_section(old_body)
    default_targets = default_wiki_targets(page["url"])
    section = existing_section or related_section_from_targets(default_targets)
    body = insert_related_section(page["body"], section)
    related_targets = WIKI_LINK_RE.findall(section or "")
    return build_frontmatter(page, today, existing_text, related_targets) + body


def load_existing_url_paths() -> dict[str, Path]:
    paths: dict[str, Path] = {}
    for path in OUT.glob("*.md"):
        fm, _body = split_frontmatter(path.read_text(encoding="utf-8"))
        url = frontmatter_scalar(fm, "url")
        if url:
            paths[url] = path
    return paths


def next_numbered_path(page: dict, used_paths: set[Path]) -> Path:
    max_num = 0
    for path in OUT.glob("*.md"):
        m = re.match(r"^(\d{3})\s+", path.name)
        if m:
            max_num = max(max_num, int(m.group(1)))
    for path in used_paths:
        m = re.match(r"^(\d{3})\s+", path.name)
        if m:
            max_num = max(max_num, int(m.group(1)))
    number = max_num + 1
    title = title_from_page_title(page["title"])
    stem = safe_file_stem(f"{number:03d} {category_prefix(page['url'])} {title}")
    path = OUT / f"{stem}.md"
    while path in used_paths or path.exists():
        number += 1
        stem = safe_file_stem(f"{number:03d} {category_prefix(page['url'])} {title}")
        path = OUT / f"{stem}.md"
    used_paths.add(path)
    return path


def extract_page(session: requests.Session, url: str, timeout: int, today: str) -> dict:
    html = fetch(session, url, timeout)
    soup_orig = BeautifulSoup(html, "lxml")
    title = soup_orig.title.get_text(" ", strip=True) if soup_orig.title else url
    title = title_from_page_title(title)

    links = []
    link_seen = set()
    for a in soup_orig.find_all("a", href=True):
        href = a["href"].strip()
        if not href or href.startswith(("javascript:", "mailto:", "tel:")):
            continue
        absu = urljoin(url, href)
        text = a.get_text(" ", strip=True)
        key = (text, absu)
        if key in link_seen:
            continue
        link_seen.add(key)
        links.append({"text": text, "url": absu})

    soup = BeautifulSoup(html, "lxml")
    for sel in [
        "script", "style", "noscript", "header", "footer", "nav", ".VPNav", ".VPSidebar",
        ".VPDocFooter", ".VPDocAside", ".VPNavBar", ".VPLocalNav", ".pager-link", ".aside", ".outline",
    ]:
        for tag in soup.select(sel):
            tag.decompose()
    main = soup.select_one("main") or soup.select_one(".VPDoc") or soup.select_one("article") or soup.body or soup
    markdown = clean_markdown(md(str(main), heading_style="ATX", bullets="-", strip=["script", "style"]))

    body = (
        f"# {title}\n\n"
        f"原始链接：{url}\n\n"
        "抓取范围：来自 `https://xiaolinnote.com/sitemap.xml`。本页保留为 raw source evidence，后续再从中拆概念卡。\n\n"
        "## 页面正文\n\n"
        f"{markdown}\n\n"
        "## 页面链接\n\n"
    )
    for l in links:
        label = l["text"] or l["url"]
        body += f"- [{label}]({l['url']})\n"
    sha = hashlib.sha256(body.encode("utf-8")).hexdigest()
    topics = topic_for(url)
    fm = "---\n"
    fm += "type: source\nsource_type: web\nsite: xiaolinnote.com\n"
    fm += "topic:" + yaml_list(topics) + "\n"
    fm += "status: inbox\n"
    fm += f"created: {today}\nupdated: {today}\n"
    fm += "url: " + json.dumps(url, ensure_ascii=False) + "\n"
    fm += "source: " + json.dumps(url, ensure_ascii=False) + "\n"
    fm += f"last_checked: {today}\nfreshness: watch\nsha256: {sha}\n"
    fm += "related:\n  - \"[[资料收集索引]]\"\n---\n\n"
    return {
        "url": url,
        "title": title,
        "topics": topics,
        "links": len(links),
        "sha256": sha,
        "body": body,
        "file_name": safe_name(url) + ".md",
    }


def build_collection_index(records: list[dict], errors: list[dict], today: str, scope: str) -> tuple[str, str]:
    ok = [r for r in records if not r.get("error")]
    by_top: dict[str, list[dict]] = {}
    for r in ok:
        top = urlparse(r["url"]).path.strip("/").split("/")[0] or "home"
        by_top.setdefault(top, []).append(r)
    body = (
        "# 小林 Note 面试题索引\n\n"
        "来源：<https://xiaolinnote.com/>\n\n"
        f"抓取日期：{today}\n\n"
        f"抓取范围：`{scope}`。读取 <https://xiaolinnote.com/sitemap.xml> 后抓取匹配 URL，并将每页正文和页面链接保存为 raw source。\n\n"
        f"- 成功页面：{len(ok)}\n"
        f"- 抓取失败页面：{len(errors)}\n"
        "- 数据目录：`raw/repos/xiaolinnote/questions/`\n\n"
        "## 分类统计\n\n"
    )
    for top, items in sorted(by_top.items()):
        body += f"- `{top}`: {len(items)} 页\n"
    body += "\n## 页面清单\n\n"
    for top, items in sorted(by_top.items()):
        body += f"### {top}\n\n"
        for r in sorted(items, key=lambda x: x["file"]):
            note = r["file"][:-3]
            body += f"- [[{note}|{Path(r['file']).stem}]] — [{r['title']}]({r['url']})\n"
        body += "\n"
    if errors:
        body += "## 抓取失败\n\n"
        for r in errors:
            body += f"- {r['url']}: `{r['error']}`\n"
    sha = hashlib.sha256(body.encode("utf-8")).hexdigest()
    fm = (
        "---\n"
        "type: source\nsource_type: web\nsite: xiaolinnote.com\n"
        "topic:\n  - interview\n  - ai\n  - agent\n  - rag\n"
        "status: inbox\n"
        f"created: {today}\nupdated: {today}\n"
        "url: \"https://xiaolinnote.com/\"\n"
        "source: \"https://xiaolinnote.com/sitemap.xml\"\n"
        f"last_checked: {today}\nfreshness: watch\nsha256: {sha}\n"
        "related:\n  - \"[[资料收集索引]]\"\n  - \"[[04 页面目录]]\"\n---\n\n"
    )
    return fm + body, sha


def update_text_file(path: Path, old_new_pairs: list[tuple[str, str]], dry_run: bool) -> bool:
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8")
    new = text
    for old, repl in old_new_pairs:
        if old in new:
            new = new.replace(old, repl)
    if new != text and not dry_run:
        path.write_text(new, encoding="utf-8")
    return new != text


def main() -> int:
    args = parse_args()
    today = date.today().isoformat()
    session = requests.Session()
    session.headers.update({"User-Agent": UA})

    sitemap_xml = fetch(session, SITEMAP, args.timeout)
    urls = [u.strip() for u in re.findall(r"<loc>(.*?)</loc>", sitemap_xml)]
    urls = [u for u in urls if urlparse(u).netloc == "xiaolinnote.com"]
    if args.scope == "ai":
        urls = [u for u in urls if urlparse(u).path.startswith("/ai/") or urlparse(u).path == "/ai"]
    seen = set()
    crawl_urls = []
    for u in urls:
        if u not in seen:
            seen.add(u)
            crawl_urls.append(u)

    OUT.mkdir(parents=True, exist_ok=True)
    existing_url_paths = load_existing_url_paths()
    used_paths = set(existing_url_paths.values())
    records: list[dict] = []
    errors: list[dict] = []
    new_pages: list[str] = []
    changed_pages: list[str] = []
    unchanged_pages: list[str] = []

    for url in crawl_urls:
        try:
            page = extract_page(session, url, args.timeout, today)
            path = existing_url_paths.get(url) or next_numbered_path(page, used_paths)
            rel = str(path.relative_to(VAULT))
            existing_sha = frontmatter_sha(path.read_text(encoding="utf-8")) if path.exists() else None
            existing_text = path.read_text(encoding="utf-8") if path.exists() else None
            page_record = {k: v for k, v in page.items() if k not in {"body", "content"}}
            page_record["file"] = rel
            page_record["file_name"] = path.name
            if not path.exists():
                new_pages.append(rel)
                if not args.dry_run:
                    path.write_text(compose_content(page, today, None), encoding="utf-8")
            elif existing_sha != page["sha256"]:
                changed_pages.append(rel)
                if not args.dry_run:
                    path.write_text(compose_content(page, today, existing_text), encoding="utf-8")
            else:
                unchanged_pages.append(rel)
            records.append(page_record)
        except Exception as exc:  # keep crawling other pages
            err = {"url": url, "error": repr(exc)}
            records.append(err)
            errors.append(err)

    collection_content, collection_sha = build_collection_index(records, errors, today, args.scope)
    collection_changed = not COLLECTION.exists() or frontmatter_sha(COLLECTION.read_text(encoding="utf-8")) != collection_sha
    if collection_changed and not args.dry_run:
        COLLECTION.write_text(collection_content, encoding="utf-8")

    manifest_data = {
        "date": today,
        "scope": args.scope,
        "sitemap_url": SITEMAP,
        "total_urls": len(crawl_urls),
        "new": new_pages,
        "changed": changed_pages,
        "unchanged_count": len(unchanged_pages),
        "errors": errors,
        "records": records,
    }
    if not args.dry_run:
        MANIFEST.write_text(json.dumps(manifest_data, ensure_ascii=False, indent=2), encoding="utf-8")

    # Keep navigation stable and compact: only the collection index is listed, not 120 individual rows.
    source_index = VAULT / "raw" / "资料收集索引.md"
    section = (
        "\n## 小林 Note 面试题\n\n"
        f"- {COLLECTION_LINK}：xiaolinnote / 小林 coding 站点 sitemap 抓取，包含 AI Agent、RAG、LLM、Tools/MCP、Git、Linux、SQL 等面试题页面。\n"
        "- 原始站点：<https://xiaolinnote.com/>\n"
        f"- 最近检查：{today}\n"
        f"- 页面数：{len(crawl_urls)}；新增 {len(new_pages)}；变化 {len(changed_pages)}；失败 {len(errors)}。\n"
        "- 数据目录：`raw/repos/xiaolinnote/questions/`，与 [[raw/repos/agent_java_offer/agent_java_offer 面试题索引]] 保持“索引页 + questions/题目页”结构一致；来源类型仍是 `web`，目录归入 `raw/repos/` 是为了统一面试题库布局。\n"
    )
    if source_index.exists():
        text = source_index.read_text(encoding="utf-8")
        old_xiaolinnote_section = r"\n## (?:小林 Note|xiaolinnote) 面试题\n\n.*?(?=\n## )"
        if not re.search(old_xiaolinnote_section, text, flags=re.S):
            text2 = text.replace("## 所有待整理资料\n", section + "\n## 所有待整理资料\n")
        else:
            text2 = re.sub(old_xiaolinnote_section, section, text, count=1, flags=re.S)
        text2 = re.sub(r"updated: \d{4}-\d{2}-\d{2}", f"updated: {today}", text2, count=1)
        text2 = re.sub(r"last_checked: \d{4}-\d{2}-\d{2}", f"last_checked: {today}", text2, count=1)
        if text2 != text and not args.dry_run:
            source_index.write_text(text2, encoding="utf-8")

    catalog = VAULT / "maps" / "04 页面目录.md"
    if catalog.exists():
        cat = catalog.read_text(encoding="utf-8")
        row = "| [[raw/repos/xiaolinnote/xiaolinnote 面试题索引]] | source | inbox | interview, ai, agent, rag | 来源证据：xiaolinnote.com sitemap 全量抓取索引，题目页在 `raw/repos/xiaolinnote/questions/` |\n"
        if COLLECTION_LINK not in cat:
            cat2 = cat.replace("| [[raw/articles/Anthropic - Building Effective Agents]] |", row + "| [[raw/articles/Anthropic - Building Effective Agents]] |")
        else:
            cat2 = cat
        cat2 = re.sub(r"updated: \d{4}-\d{2}-\d{2}", f"updated: {today}", cat2, count=1)
        if cat2 != cat and not args.dry_run:
            catalog.write_text(cat2, encoding="utf-8")

    main_index = VAULT / "index.md"
    if main_index.exists():
        idx = main_index.read_text(encoding="utf-8")
        idx2 = idx
        if COLLECTION_LINK not in idx2:
            idx2 = idx2.replace("- [[资料收集索引]]\n", f"- [[资料收集索引]]\n- {COLLECTION_LINK}\n")
        idx2 = re.sub(r"updated: \d{4}-\d{2}-\d{2}", f"updated: {today}", idx2, count=1)
        if idx2 != idx and not args.dry_run:
            main_index.write_text(idx2, encoding="utf-8")

    if not args.no_log and not args.dry_run:
        log = VAULT / "log.md"
        if log.exists() and (new_pages or changed_pages or errors or collection_changed):
            log_text = log.read_text(encoding="utf-8")
            log_text = re.sub(r"updated: \d{4}-\d{2}-\d{2}", f"updated: {today}", log_text, count=1)
            entry = (
                f"\n## [{today}] source-update | 小林 Note sitemap 面试题\n\n"
                f"- Source: {COLLECTION_LINK}\n"
                f"- Scope: `{args.scope}`; checked {len(crawl_urls)} sitemap URLs.\n"
                f"- Result: new {len(new_pages)}, changed {len(changed_pages)}, unchanged {len(unchanged_pages)}, errors {len(errors)}.\n"
                "- Updated navigation: [[资料收集索引]], [[04 页面目录]], [[index]]\n"
                "- Boundary: this is raw evidence refresh; changed pages still need explicit wiki/concept digestion if their content matters.\n"
            )
            log.write_text(log_text + entry, encoding="utf-8")

    report = {
        "dry_run": args.dry_run,
        "scope": args.scope,
        "checked_urls": len(crawl_urls),
        "new": len(new_pages),
        "changed": len(changed_pages),
        "unchanged": len(unchanged_pages),
        "errors": len(errors),
        "collection_index": str(COLLECTION),
        "manifest": str(MANIFEST),
        "new_files": new_pages[:20],
        "changed_files": changed_pages[:20],
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
