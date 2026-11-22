#!/usr/bin/env python3
"""
FlowForge — Documentation Validation Script
Verifies that all required project documents exist and are non-empty.
Run: python check_docs.py
"""

import os
import sys

REQUIRED_DOCS = [
    "docs/prd.md",
    "docs/architecture.md",
    "docs/rules.md",
    "docs/phases.md",
    "docs/design.md",
    "docs/memory.md",
    "docs/decisions.md",
    "docs/flow.md",
]

REQUIRED_ROOT_FILES = [
    "README.md",
    "TEAM_PLAN_AND_PROMPTS.md",
    ".gitignore",
]

def check_files(file_list, label):
    """Check that each file exists and is non-empty."""
    passed = 0
    failed = 0
    for filepath in file_list:
        if not os.path.exists(filepath):
            print(f"  MISSING  {filepath}")
            failed += 1
        elif os.path.getsize(filepath) == 0:
            print(f"  EMPTY    {filepath}")
            failed += 1
        else:
            size = os.path.getsize(filepath)
            print(f"  OK       {filepath} ({size} bytes)")
            passed += 1
    return passed, failed

def main():
    print("=" * 50)
    print("FlowForge Documentation Check")
    print("=" * 50)

    total_passed = 0
    total_failed = 0

    print(f"\n--- Required docs ({len(REQUIRED_DOCS)} files) ---")
    p, f = check_files(REQUIRED_DOCS, "docs")
    total_passed += p
    total_failed += f

    print(f"\n--- Required root files ({len(REQUIRED_ROOT_FILES)} files) ---")
    p, f = check_files(REQUIRED_ROOT_FILES, "root")
    total_passed += p
    total_failed += f

    # Check optional but expected files
    optional_files = [
        ".github/PULL_REQUEST_TEMPLATE.md",
    ]
    print(f"\n--- Optional files ({len(optional_files)} files) ---")
    for filepath in optional_files:
        if os.path.exists(filepath):
            print(f"  OK       {filepath}")
        else:
            print(f"  MISSING  {filepath} (optional)")

    print(f"\n{'=' * 50}")
    print(f"Results: {total_passed} passed, {total_failed} failed")
    print(f"{'=' * 50}")

    if total_failed > 0:
        print("\nFAILED: Fix missing/empty files before starting feature work.")
        sys.exit(1)
    else:
        print("\nPASSED: All required documentation is present.")
        sys.exit(0)

if __name__ == "__main__":
    main()
