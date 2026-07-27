#!/usr/bin/env python3
"""Build the configured Taiwan KM meeting draft reproducibly."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path
from typing import Any

import yaml
from dsw_km_translation_tool.km_release import load_km_source_repository_config
from dsw_km_translation_tool.legal_review import LegalReviewError, build_legal_draft


def build_argument_parser() -> argparse.ArgumentParser:
    """Build the command-line parser."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    parser.add_argument("--tooling-repo", type=Path, required=True)
    parser.add_argument("--source-km", type=Path, required=True)
    parser.add_argument(
        "--output",
        type=Path,
        help="Optional output override used by reproducibility checks.",
    )
    return parser


def main() -> None:
    """Build the configured draft after validating the tooling checkout."""

    args = build_argument_parser().parse_args()
    root = args.repo_root.resolve()
    config_path = root / "km-repository.yml"
    payload = _load_config(config_path)
    source_config = load_km_source_repository_config(config_path)
    draft = _mapping(payload, "draft")
    tooling = _mapping(payload, "tooling")
    tooling_repo = args.tooling_repo.resolve()
    _validate_tooling_checkout(
        tooling_repo=tooling_repo,
        expected_ref=_string(tooling, "ref"),
    )

    output = args.output.resolve() if args.output else root / source_config.bundle_path
    result = build_legal_draft(
        km_path=args.source_km.resolve(),
        mapping_path=root / _safe_relative_path(draft, "legal_mapping_path"),
        output_path=output,
        organization_id=source_config.organization_id,
        km_id=source_config.km_id,
        version=_string(draft, "version"),
        name=source_config.name,
        description=_string(draft, "description"),
        license_id=_string(draft, "license"),
        readme=(root / _safe_relative_path(draft, "package_readme_path")).read_text(
            encoding="utf-8"
        ),
    )
    print(
        f"Built {result.package_id} from {result.parent_package_id} "
        f"with {result.event_count} legal edit events: {result.output_path}"
    )


def _load_config(path: Path) -> dict[str, Any]:
    try:
        payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as error:
        raise SystemExit(f"Unable to read {path}: {error}") from error
    if not isinstance(payload, dict):
        raise SystemExit(f"{path} must contain a YAML mapping")
    return payload


def _mapping(payload: dict[str, Any], key: str) -> dict[str, Any]:
    value = payload.get(key)
    if not isinstance(value, dict):
        raise SystemExit(f"km-repository.yml {key} must be a mapping")
    return value


def _string(payload: dict[str, Any], key: str) -> str:
    value = payload.get(key)
    if not isinstance(value, str) or not value.strip():
        raise SystemExit(f"km-repository.yml {key} must be a non-empty string")
    return value.strip()


def _safe_relative_path(payload: dict[str, Any], key: str) -> Path:
    value = Path(_string(payload, key))
    if value.is_absolute() or ".." in value.parts:
        raise SystemExit(f"km-repository.yml {key} must be a safe relative path")
    return value


def _validate_tooling_checkout(*, tooling_repo: Path, expected_ref: str) -> None:
    try:
        result = subprocess.run(
            ["git", "-C", str(tooling_repo), "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError) as error:
        raise SystemExit(f"Unable to inspect tooling checkout {tooling_repo}: {error}") from error
    actual_ref = result.stdout.strip()
    if actual_ref != expected_ref:
        raise SystemExit(
            f"Tooling checkout is {actual_ref}, but km-repository.yml pins {expected_ref}"
        )


if __name__ == "__main__":
    try:
        main()
    except (OSError, LegalReviewError) as error:
        raise SystemExit(str(error)) from error
