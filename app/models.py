from pydantic import BaseModel, Field
from datetime import date
from typing import List


class Car(BaseModel):
    id: str
    brand: str
    model: str


class BookingCreate(BaseModel):
    car_id: str = Field(..., min_length=1)
    date: date
    customer_name: str = Field(..., min_length=1)


class Booking(BaseModel):
    id: str
    car_id: str
    date: date
    customer_name: str


class AvailableCarsResponse(BaseModel):
    date: date
    cars: List[Car]
