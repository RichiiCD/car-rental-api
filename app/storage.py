import json
import os
from pathlib import Path

_DEFAULT_DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def _data_dir() -> Path:
    # Read at runtime (not import time) so tests can monkeypatch DATA_DIR reliably.
    return Path(os.environ.get("DATA_DIR", str(_DEFAULT_DATA_DIR)))


def _cars_file() -> Path:
    return _data_dir() / "cars.json"


def _bookings_file() -> Path:
    return _data_dir() / "bookings.json"

