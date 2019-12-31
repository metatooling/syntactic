"""An example module providing a transformer."""


def transform_bangbang(source: str) -> str:
    """Replace !! with a greeting."""
    return source.replace("!!", 'print("hello")')


def transform_lambda(source: str) -> str:
    """Replace unicode lambda."""
    return source.replace("λ", "lambda")
