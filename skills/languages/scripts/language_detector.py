#!/usr/bin/env python3
"""Cloudflare Project Language Detector."""

import json
from pathlib import Path


def detect_languages(path: str) -> dict:
    """Detect programming languages used in Cloudflare project."""
    project = Path(path)

    languages = {
        "typescript": False,
        "javascript": False,
        "rust": False,
        "python": False,
        "wasm": False
    }

    # Check for TypeScript
    if (project / "tsconfig.json").exists():
        languages["typescript"] = True

    # Check for package.json (JS/TS)
    pkg = project / "package.json"
    if pkg.exists():
        content = json.loads(pkg.read_text())
        deps = {**content.get("dependencies", {}), **content.get("devDependencies", {})}
        if "typescript" in deps:
            languages["typescript"] = True
        languages["javascript"] = True

    # Check for Rust (WASM)
    if (project / "Cargo.toml").exists():
        languages["rust"] = True
        languages["wasm"] = True

    # Check for Python (Pyodide)
    if (project / "requirements.txt").exists() or (project / "pyproject.toml").exists():
        languages["python"] = True

    # Count source files
    ts_files = len(list(project.rglob("*.ts")))
    js_files = len(list(project.rglob("*.js")))
    rs_files = len(list(project.rglob("*.rs")))

    return {
        "detected": languages,
        "file_counts": {
            "typescript": ts_files,
            "javascript": js_files,
            "rust": rs_files
        },
        "primary": "typescript" if ts_files > 0 else "javascript" if js_files > 0 else "unknown"
    }


def main():
    import sys
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    print(json.dumps(detect_languages(path), indent=2))


if __name__ == "__main__":
    main()
