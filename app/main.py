from fastapi import FastAPI
import logging

from app.routes.cars import router as cars_router
from app.routes.bookings import router as bookings_router

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger("car-rental")

app = FastAPI(title="Car Rental API")

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(cars_router)
app.include_router(bookings_router)
