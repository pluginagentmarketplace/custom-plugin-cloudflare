#!/usr/bin/env python3
"""Cloudflare AI Model and Emerging Tech Validator."""

import json
from pathlib import Path
from dataclasses import dataclass


@dataclass
class AIServiceCheck:
    workers_ai: bool = False
    vectorize: bool = False
    constellation: bool = False
    durable_objects: bool = False


def validate_emerging_tech(path: str) -> dict:
    """Validate emerging technology setup in Cloudflare project."""
    project = Path(path)
    check = AIServiceCheck()

    # Check wrangler.toml for AI bindings
    wrangler = project / "wrangler.toml"
    if wrangler.exists():
        content = wrangler.read_text().lower()
        check.workers_ai = "ai" in content and "binding" in content
        check.vectorize = "vectorize" in content
        check.durable_objects = "durable_objects" in content

    # Check for constellation config
    constellation_config = project / "constellation.json"
    check.constellation = constellation_config.exists()

    return {
        "workers_ai": check.workers_ai,
        "vectorize": check.vectorize,
        "constellation": check.constellation,
        "durable_objects": check.durable_objects,
        "ai_ready": check.workers_ai or check.constellation,
        "edge_ready": check.durable_objects
    }


def main():
    import sys
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    print(json.dumps(validate_emerging_tech(path), indent=2))


if __name__ == "__main__":
    main()
