import os
import json
from pathlib import Path
from fastapi.testclient import TestClient


def test_create_booking_conflict(tmp_path: Path, monkeypatch):
    monkeypatch.setenv("DATA_DIR", str(tmp_path))

    from app.main import app  # importar DESPUÉS
    client = TestClient(app)

    # Crear data inicial
    (tmp_path / "cars.json").write_text(json.dumps([
        {"id": "car_1", "brand": "Toyota", "model": "Corolla"}
    ]), encoding="utf-8")

    (tmp_path / "bookings.json").write_text("[]", encoding="utf-8")

    client = TestClient(app)

    payload = {"car_id": "car_1", "date": "2026-01-20", "customer_name": "Ana"}

    r1 = client.post("/bookings", json=payload)
    assert r1.status_code == 201

    r2 = client.post("/bookings", json=payload)
    assert r2.status_code == 409
