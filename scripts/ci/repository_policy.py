#!/usr/bin/env python3
"""Validate the repository's tracked-file policy without network access."""
from __future__ import annotations

import subprocess
import sys
from pathlib import PurePosixPath

REQUIRED = {"README.md", ".gitignore"}
FORBIDDEN_PARTS = {
    ".env",
    ".session",
    "browser-data",
    "browser-profile",
    "credentials",
    "cookies",
}
FORBIDDEN_SUFFIXES = {".pem", ".key", ".pfx", ".p12"}


def tracked_paths() -> list[PurePosixPath]:
    result = subprocess.run(
        ["git", "ls-files", "-z"], check=True, capture_output=True, text=False
    )
    return [PurePosixPath(item.decode()) for item in result.stdout.split(b"\0") if item]


def main() -> int:
    paths = tracked_paths()
    names = {path.as_posix() for path in paths}
    missing = sorted(REQUIRED - names)
    violations: list[str] = []

    for path in paths:
        lowered = [part.lower() for part in path.parts]
        if any(part in FORBIDDEN_PARTS for part in lowered):
            violations.append(f"forbidden tracked path: {path}")
        if path.suffix.lower() in FORBIDDEN_SUFFIXES:
            violations.append(f"forbidden credential-like suffix: {path}")

    if missing:
        violations.extend(f"missing required file: {path}" for path in missing)

    if violations:
        print("Repository policy validation failed:")
        print("\n".join(f"- {item}" for item in violations))
        return 1

    print(f"Repository policy validation passed for {len(paths)} tracked paths.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
