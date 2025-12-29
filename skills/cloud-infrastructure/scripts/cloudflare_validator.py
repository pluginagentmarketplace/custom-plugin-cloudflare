#!/usr/bin/env python3
"""
Cloudflare Configuration Validator - Cloudflare Plugin
Validates Cloudflare Workers, Pages, R2, and D1 configurations.
"""

import json
import os
from pathlib import Path
from dataclasses import dataclass, field


@dataclass
class CloudflareValidation:
    """Cloudflare validation results."""
    has_wrangler: bool = False
    has_workers: bool = False
    has_pages: bool = False
    has_r2: bool = False
    has_d1: bool = False
    issues: list = field(default_factory=list)


class CloudflareValidator:
    """Validate Cloudflare project configuration."""

    def __init__(self, project_path: str):
        self.project_path = Path(project_path)

    def validate(self) -> dict:
        """Validate Cloudflare configuration."""
        validation = CloudflareValidation()

        # Check for wrangler.toml
        wrangler_file = self.project_path / "wrangler.toml"
        if wrangler_file.exists():
            validation.has_wrangler = True
            self._validate_wrangler(wrangler_file, validation)
        else:
            validation.issues.append("Missing wrangler.toml")

        # Check for workers
        src_path = self.project_path / "src"
        if src_path.exists():
            worker_files = list(src_path.glob("*.ts")) + list(src_path.glob("*.js"))
            validation.has_workers = len(worker_files) > 0

        return self._generate_report(validation)

    def _validate_wrangler(self, wrangler_file: Path, validation: CloudflareValidation):
        """Validate wrangler.toml configuration."""
        try:
            content = wrangler_file.read_text()

            # Check for R2 bindings
            if "[[r2_buckets]]" in content:
                validation.has_r2 = True

            # Check for D1 bindings
            if "[[d1_databases]]" in content:
                validation.has_d1 = True

            # Check for required fields
            if "name" not in content:
                validation.issues.append("Missing 'name' in wrangler.toml")
            if "main" not in content:
                validation.issues.append("Missing 'main' entry point")

        except Exception as e:
            validation.issues.append(f"Error reading wrangler.toml: {e}")

    def _generate_report(self, validation: CloudflareValidation) -> dict:
        """Generate validation report."""
        return {
            "cloudflare": {
                "wrangler_configured": validation.has_wrangler,
                "workers": validation.has_workers,
                "r2_storage": validation.has_r2,
                "d1_database": validation.has_d1,
            },
            "issues": validation.issues,
            "ready_for_deployment": len(validation.issues) == 0,
        }


def main():
    import sys
    project_path = sys.argv[1] if len(sys.argv) > 1 else "."
    validator = CloudflareValidator(project_path)
    report = validator.validate()
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
