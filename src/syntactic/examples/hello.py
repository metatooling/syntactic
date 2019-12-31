"""An example module providing a transformer."""


def transform(source: str) -> str:
    """Replace !! with a greeting."""
    return source.replace("!!", 'print("hello")')
