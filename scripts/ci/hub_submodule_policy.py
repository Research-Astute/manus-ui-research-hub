#!/usr/bin/env python3
"""Validate the hub's pinned research and development submodule declarations."""
from __future__ import annotations

import configparser
import subprocess
import sys
from pathlib import Path

EXPECTED = {
    "research/manus-public-ui-research": "https://github.com/search-astute-ly/manus-public-ui-research.git",
    "development/manus-ui-adapter-lab": "https://github.com/Research-Astute/manus-ui-adapter-lab.git",
}


def gitlink_paths() -> set[str]:
    result = subprocess.run(
        ["git", "ls-files", "--stage"], check=True, capture_output=True, text=True
    )
    return {
        line.split("\t", 1)[1]
        for line in result.stdout.splitlines()
        if line.startswith("160000 ") and "\t" in line
    }


def main() -> int:
    parser = configparser.ConfigParser()
    parser.read(Path(".gitmodules"))
    actual: dict[str, str] = {}
    for section in parser.sections():
        path = parser.get(section, "path", fallback="")
        url = parser.get(section, "url", fallback="")
        actual[path] = url

    errors: list[str] = []
    if actual != EXPECTED:
        errors.append(f"unexpected submodule mapping: {actual}")
    links = gitlink_paths()
    if links != set(EXPECTED):
        errors.append(f"unexpected gitlink paths: {sorted(links)}")

    if errors:
        print("Hub submodule validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1

    print("Hub submodule declarations and gitlinks are pinned to the approved lanes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
