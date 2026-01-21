from fastapi import APIRouter
from datetime import date

import logging

logger = logging.getLogger("car-rental")

router = APIRouter(prefix="/cars", tags=["cars"])


@router.get("/available")
def available_cars(date: date):
    pass