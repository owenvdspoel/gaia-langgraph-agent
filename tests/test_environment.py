
from importlib.metadata import version


def test_core_dependencies():
    packages = [
        "langchain",
        "langgraph",
        "langchain-google-genai",
    ]

    for package in packages:
        assert version(package)
