"""Provides something for __syntax__ imports to import.
"""


def __getattr__(name: str) -> None:
    """Return ``None`` without doing anything."""
    return None
