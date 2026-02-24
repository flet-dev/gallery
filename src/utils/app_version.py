import os
import tomllib
from pathlib import Path


def _version_from_pyproject() -> str:
    pyproject_path = Path(__file__).resolve().parents[2] / "pyproject.toml"
    with pyproject_path.open("rb") as f:
        data = tomllib.load(f)
    return data["project"]["version"]


def get_app_version() -> str:
    return os.getenv("APP_VERSION") or _version_from_pyproject()
