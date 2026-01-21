"""
Simple JSON file storage.

- Uses DATA_DIR env var to allow tests to run against a temporary directory.
- Writes bookings.json atomically (write temp file + replace) to avoid partial writes.
"""

import json
import os
from pathlib import Path
from typing import Any

_DEFAULT_DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def _data_dir() -> Path:
    # Read at runtime (not import time) so tests can monkeypatch DATA_DIR reliably.
    return Path(os.environ.get("DATA_DIR", str(_DEFAULT_DATA_DIR)))


def _cars_file() -> Path:
    return _data_dir() / "cars.json"


def _bookings_file() -> Path:
    return _data_dir() / "bookings.json"


def _read_json(path: Path) -> Any:
    # Missing file => treat as empty list (simple storage for this kata).
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _write_json(path: Path, data: Any) -> None:
    # Atomic write: prevents corrupted JSON if the process is interrupted.
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    tmp.replace(path)


def load_cars() -> list[dict]:
    return _read_json(_cars_file())


def load_bookings() -> list[dict]:
    return _read_json(_bookings_file())


def save_bookings(bookings: list[dict]) -> None:
    _write_json(_bookings_file(), bookings)
