#!/usr/bin/env python3
"""Cloudflare Architecture and System Design Validator."""

import json
from pathlib import Path
from dataclasses import dataclass, field
from typing import List


@dataclass
class ArchitectureAnalysis:
    services: List[str] = field(default_factory=list)
    patterns: List[str] = field(default_factory=list)
    score: int = 0


def validate_architecture(path: str) -> dict:
    """Validate Cloudflare architecture setup."""
    project = Path(path)
    analysis = ArchitectureAnalysis()

    wrangler = project / "wrangler.toml"
    if wrangler.exists():
        content = wrangler.read_text().lower()

        # Detect services
        services_map = {
            "kv_namespaces": "KV Storage",
            "d1_databases": "D1 Database",
            "r2_buckets": "R2 Object Storage",
            "durable_objects": "Durable Objects",
            "queues": "Queues",
            "vectorize": "Vectorize",
            "ai": "Workers AI"
        }

        for key, name in services_map.items():
            if key in content:
                analysis.services.append(name)
                analysis.score += 15

        # Detect patterns
        if "durable_objects" in content:
            analysis.patterns.append("Stateful Edge")
        if "queues" in content:
            analysis.patterns.append("Async Processing")
        if "d1" in content and "kv" in content:
            analysis.patterns.append("Hybrid Storage")

    # Check for Pages
    if (project / "functions").exists():
        analysis.services.append("Pages Functions")
        analysis.patterns.append("Fullstack Edge")
        analysis.score += 20

    return {
        "services": analysis.services,
        "patterns": analysis.patterns,
        "architecture_score": min(analysis.score, 100),
        "production_ready": analysis.score >= 50,
        "recommendation": "Add caching layer" if "KV Storage" not in analysis.services else "Well architected"
    }


def main():
    import sys
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    print(json.dumps(validate_architecture(path), indent=2))


if __name__ == "__main__":
    main()
