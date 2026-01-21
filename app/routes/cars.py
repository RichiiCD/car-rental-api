from fastapi import APIRouter
from datetime import date

from app.models import AvailableCarsResponse
from app.storage import load_cars, load_bookings
import logging

logger = logging.getLogger("car-rental")

router = APIRouter(prefix="/cars", tags=["cars"])


@router.get("/available", response_model=AvailableCarsResponse)
def available_cars(date: date):
    # A car is available if it has no booking for the requested date.
    cars = load_cars()
    bookings = load_bookings()

    booked_car_ids = {
        b["car_id"] for b in bookings
        if b.get("date") == date.isoformat()
    }

    available = [c for c in cars if c["id"] not in booked_car_ids]
    logger.info("available_cars date=%s available=%d", date.isoformat(), len(available))

    return {"date": date, "cars": available}
