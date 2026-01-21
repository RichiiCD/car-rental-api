from fastapi import APIRouter, HTTPException
from uuid import uuid4

from app.models import BookingCreate, Booking
from app.storage import load_cars, load_bookings, save_bookings
import logging

logger = logging.getLogger("car-rental")

router = APIRouter(prefix="/bookings", tags=["bookings"])


@router.post("", status_code=201, response_model=Booking)
def create_booking(payload: BookingCreate):
    # Business rule: car must exist.
    # (cars.json is the source of truth for known car IDs)
    cars = load_cars()
    if not any(c["id"] == payload.car_id for c in cars):
        raise HTTPException(status_code=404, detail="car_id not found")

    bookings = load_bookings()
    payload_date = payload.date.isoformat()

    # Business rule: a car can only be booked once per date.
    conflict = any(
        b["car_id"] == payload.car_id and b.get("date") == payload_date
        for b in bookings
    )
    if conflict:
        raise HTTPException(status_code=409, detail="car already booked for that date")

    new_booking = {
        "id": str(uuid4()),
        "car_id": payload.car_id,
        "date": payload_date,
        "customer_name": payload.customer_name,
    }
    bookings.append(new_booking)
    save_bookings(bookings)
    logger.info("create_booking car_id=%s date=%s", payload.car_id, payload_date)

    return new_booking
