from fastapi import FastAPI
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger("car-rental")

app = FastAPI(title="Car Rental API")

@app.get("/health")
def health():
    return {"status": "ok"}

