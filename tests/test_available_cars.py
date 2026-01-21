import json
from pathlib import Path
from fastapi.testclient import TestClient

from app.main import app

def test_available_cars_excludes_booked(tmp_path: Path, monkeypatch):
    monkeypatch.setenv("DATA_DIR", str(tmp_path))

    (tmp_path / "cars.json").write_text(json.dumps([
        {"id": "car_1", "brand": "Toyota", "model": "Corolla"},
        {"id": "car_2", "brand": "Seat", "model": "Ibiza"},
    ]), encoding="utf-8")

    (tmp_path / "bookings.json").write_text(json.dumps([
        {"id": "b1", "car_id": "car_1", "date": "2026-01-20", "customer_name": "Ana"}
    ]), encoding="utf-8")

    client = TestClient(app)

    r = client.get("/cars/available", params={"date": "2026-01-20"})
    assert r.status_code == 200
    data = r.json()
    assert data["date"] == "2026-01-20"
    ids = [c["id"] for c in data["cars"]]
    assert "car_1" not in ids
    assert "car_2" in ids
