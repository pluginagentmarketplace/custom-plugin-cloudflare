#!/usr/bin/env python3
"""Project Structure Analyzer."""

import json
from pathlib import Path
from dataclasses import dataclass


@dataclass
class ProjectAnalysis:
    project_type: str = "unknown"
    frontend_framework: str = ""
    backend_framework: str = ""
    has_tests: bool = False


class ProjectAnalyzer:
    def __init__(self, path: str):
        self.path = Path(path)

    def analyze(self) -> dict:
        analysis = ProjectAnalysis()

        # Check package.json
        pkg = self.path / "package.json"
        if pkg.exists():
            content = json.loads(pkg.read_text())
            deps = content.get("dependencies", {})

            if "react" in deps:
                analysis.frontend_framework = "react"
            if "express" in deps or "fastify" in deps:
                analysis.backend_framework = "node"

        analysis.has_tests = (self.path / "tests").exists()

        return {
            "type": analysis.project_type,
            "frontend": analysis.frontend_framework,
            "backend": analysis.backend_framework,
            "has_tests": analysis.has_tests
        }


def main():
    import sys
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    print(json.dumps(ProjectAnalyzer(path).analyze(), indent=2))


if __name__ == "__main__":
    main()
