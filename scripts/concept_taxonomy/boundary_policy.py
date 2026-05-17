"""Shared non-taxonomy boundary policy for concept relation writeback.

These pairs are forbidden as ``up`` edges because they cross semantic layers:
representation/feature -> method family -> route/component -> strategy.
They may still be useful as typed ``relations`` or ordinary adjacency.
"""
from __future__ import annotations

import paths
NON_TAXONOMY_BOUNDARIES: dict[tuple[str, str], dict[str, str]] = {
    ("TF-IDF", "RAG"): {
        "kind": "representation_vs_application",
        "safe_relation": "related_to",
        "rationale": "TF-IDF is a sparse lexical weighting/representation used in retrieval contexts; it is not a RAG subtype.",
    },
    ("TF-IDF", "Retriever"): {
        "kind": "feature_vs_component",
        "safe_relation": "foundational_for -> Sparse Retrieval",
        "rationale": "TF-IDF can supply sparse lexical scoring intuition, but it is not a retriever component subtype.",
    },
    ("TF-IDF", "Sparse Retrieval"): {
        "kind": "foundation_vs_family",
        "safe_relation": "foundational_for",
        "rationale": "TF-IDF is a foundational sparse lexical weighting method; Sparse Retrieval is the broader retrieval family.",
    },
    ("TF-IDF", "Multi-Route Retrieval"): {
        "kind": "feature_vs_strategy",
        "safe_relation": "foundational_for -> Sparse Retrieval; Sparse Retrieval composed_into -> Multi-Route Retrieval",
        "rationale": "TF-IDF itself is not a multi-route retrieval route or strategy; a sparse retrieval route may use TF-IDF/BM25-style signals inside multi-route retrieval.",
    },
    ("BM25", "Multi-Route Retrieval"): {
        "kind": "algorithm_vs_strategy",
        "safe_relation": "composed_into via Sparse Retrieval",
        "rationale": "BM25 is a sparse retrieval scoring function/representative route signal, not a multi-route retrieval subtype.",
    },
    ("Sparse Retrieval", "Multi-Route Retrieval"): {
        "kind": "route_vs_strategy",
        "safe_relation": "composed_into",
        "rationale": "Sparse Retrieval can be one route inside Multi-Route Retrieval, but a route/component is not a child taxonomy of the orchestration strategy.",
    },
    ("Dense Retrieval", "Multi-Route Retrieval"): {
        "kind": "route_vs_strategy",
        "safe_relation": "composed_into",
        "rationale": "Dense Retrieval can be one route inside Multi-Route Retrieval, but a route/component is not a child taxonomy of the orchestration strategy.",
    },
    ("Reranking", "Multi-Route Retrieval"): {
        "kind": "stage_vs_strategy",
        "safe_relation": "composes_with",
        "rationale": "Reranking is a downstream ordering stage over candidates; it is not a recall route or subtype of Multi-Route Retrieval.",
    },
    ("Top-K", "Multi-Route Retrieval"): {
        "kind": "selection_rule_vs_strategy",
        "safe_relation": "related_to",
        "rationale": "Top-K is a candidate selection/ranking cutoff, not a multi-route retrieval subtype.",
    },
    ("Multi-Route Retrieval", "Sparse Retrieval"): {
        "kind": "strategy_vs_route",
        "safe_relation": "composes_with",
        "rationale": "Multi-Route Retrieval may compose Sparse Retrieval as one route; the strategy is not a child of the route.",
    },
    ("Multi-Route Retrieval", "BM25"): {
        "kind": "strategy_vs_algorithm",
        "safe_relation": "composes_with -> Sparse Retrieval/BM25 route",
        "rationale": "Multi-Route Retrieval may include a BM25 sparse route; the strategy is not a BM25 subtype.",
    },
    ("Multi-Route Retrieval", "Hybrid Search"): {
        "kind": "strategy_vs_common_shape",
        "safe_relation": "related_to",
        "rationale": "Hybrid Search is a common dense+sparse shape inside the wider multi-route retrieval design space; this should be explained as relation, not forced into up.",
    },
    ("Hybrid Search", "Sparse Retrieval"): {
        "kind": "composition_vs_component",
        "safe_relation": "composes_with",
        "rationale": "Hybrid Search composes a sparse retrieval side; it is not a Sparse Retrieval subtype.",
    },
    ("Hybrid Search", "Dense Retrieval"): {
        "kind": "composition_vs_component",
        "safe_relation": "composes_with",
        "rationale": "Hybrid Search composes a dense retrieval side; it is not a Dense Retrieval subtype.",
    },
}

FORBIDDEN_UP_PAIRS = frozenset(NON_TAXONOMY_BOUNDARIES)


def policy_rows() -> list[dict[str, str]]:
    """Return stable machine-readable rows for ledger/report output."""
    return [
        {
            "source": source,
            "target": target,
            "boundary_kind": boundary["kind"],
            "safe_relation": boundary["safe_relation"],
            "rationale": boundary["rationale"],
            "guardrail": "forbidden_as_up",
        }
        for (source, target), boundary in sorted(NON_TAXONOMY_BOUNDARIES.items())
    ]
