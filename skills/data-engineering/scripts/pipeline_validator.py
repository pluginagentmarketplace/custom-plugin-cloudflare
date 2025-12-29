#!/usr/bin/env python3
"""Data Pipeline Validator."""

import json
from pathlib import Path


def validate_pipeline(path: str) -> dict:
    project = Path(path)

    has_dags = (project / "dags").exists()
    has_dbt = (project / "dbt_project.yml").exists()

    return {
        "airflow_dags": has_dags,
        "dbt_project": has_dbt,
        "ready": has_dags or has_dbt
    }


def main():
    import sys
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    print(json.dumps(validate_pipeline(path), indent=2))


if __name__ == "__main__":
    main()
