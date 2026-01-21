# Car Rental API (FastAPI)

Simple **REST API** for a car rental service built with **FastAPI**.

## Requirements

- **Python 3.12**
- **pip**
- (Optional) **Docker** / **Docker Compose**

## Setup (local)

Create and activate a virtual environment:

```bash
python3.12 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## Run the API (local)

Start the server:

```bash
uvicorn app.main:app --reload
```

Open:

- **Swagger UI**: http://127.0.0.1:8000/docs
- **Health check**: http://127.0.0.1:8000/health

## Storage (File-based JSON)

Data is persisted in JSON files under the `data/` directory:

- `data/cars.json` — list of cars
- `data/bookings.json` — list of bookings

Bookings are appended to `data/bookings.json` when created.

The storage layer supports changing the data directory via environment variable:

- `DATA_DIR` (defaults to `./data`)

This is used by tests (temporary directory) and by Docker (mounted volume).

## Endpoints

### List available cars for a given date

**GET** `/cars/available?date=YYYY-MM-DD`

Example:

```bash
curl "http://127.0.0.1:8000/cars/available?date=2026-01-20"
```

Response (example):

```json
{
  "date": "2026-01-20",
  "cars": [{ "id": "car_2", "brand": "Seat", "model": "Ibiza" }]
}
```

### Create a booking

**POST** `/bookings`

Example:

```bash
curl -X POST "http://127.0.0.1:8000/bookings"   -H "Content-Type: application/json"   -d '{"car_id":"car_1","date":"2026-01-20","customer_name":"Ana Garcia"}'
```

Response (example):

```json
{
  "id": "b2f1a1d0-7d8b-4e07-9c1f-0d9a5b0b2e33",
  "car_id": "car_1",
  "date": "2026-01-20",
  "customer_name": "Ana Garcia"
}
```

## Error cases

- **404 Not Found** when `car_id` does not exist
- **409 Conflict** when the same car is already booked for the same date
- **422 Unprocessable Entity** when request validation fails (e.g. invalid date format)

## Logging

The service uses basic application logging (**stdout**) to log key actions such as listing availability and creating bookings.

## Tests

To avoid needing `PYTHONPATH=.` when running tests, create a `pytest.ini` file in the project root:

```ini
[pytest]
pythonpath = .
```

Run tests:

```bash
pytest -q
```
