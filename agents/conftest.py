# conftest.py
import warnings


def pytest_configure(config):
    # Pydantic v2 serializer warnings are often triggered by LLM wrappers / tracing objects
    # and are typically non-fatal noise for these labs.
    warnings.filterwarnings(
        "ignore",
        category=UserWarning,
        module=r"pydantic\.main",
    )

    # If the above doesn't catch due to module differences, this message-based filter is a fallback.
    # Note: warnings uses re.match (anchored), so we use .* to match anywhere in the message.
    warnings.filterwarnings(
        "ignore",
        message=r".*Pydantic serializer warnings.*",
        category=UserWarning,
    )
