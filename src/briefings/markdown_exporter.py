"""Markdown exporter."""


def export_markdown(title: str, body: str) -> str:
    """Return Markdown briefing text."""
    return f"# {title}\n\n{body}\n"

