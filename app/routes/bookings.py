from fastapi import APIRouter, HTTPException
from uuid import uuid4

import logging

logger = logging.getLogger("car-rental")

router = APIRouter(prefix="/bookings", tags=["bookings"])


@router.post("", status_code=201)
def create_booking(payload: BookingCreate):
    pass
