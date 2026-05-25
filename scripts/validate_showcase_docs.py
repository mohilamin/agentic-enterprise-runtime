"""Validate required V0.3 showcase documentation exists."""

from pathlib import Path

REQUIRED_FILES = [
    "docs/screenshots/README.md",
    "docs/interview/five-minute-demo-script.md",
    "docs/interview/ten-minute-technical-walkthrough.md",
    "docs/one-pagers/architecture-one-pager.md",
    "docs/one-pagers/recruiter-one-pager.md",
    "docs/one-pagers/technical-reviewer-one-pager.md",
    "docs/blog/technical-blog-draft.md",
    "docs/launch/linkedin-launch-sequence.md",
    "docs/launch/github-repo-setup.md",
    "docs/launch/portfolio-landing-update.md",
    "docs/resume/flagship-resume-bullets.md",
    "docs/v03-showcase-polish.md",
]


def main() -> int:
    """Exit nonzero if any required showcase docs are missing."""
    missing = [file for file in REQUIRED_FILES if not Path(file).exists()]
    if missing:
        print("Missing V0.3 showcase docs:")
        for file in missing:
            print(f"- {file}")
        return 1
    print(f"V0.3 showcase docs validation passed: {len(REQUIRED_FILES)} required files found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
