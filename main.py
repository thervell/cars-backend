from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:8080"],
    allow_methods = ["*"],
    allow_headers = ["*"]
)

cars_db = [
    {"id": 1, "title": "Audi", "text": "Немецкое качество и комфорт", "img": "audi.jpg"},
    {"id": 2, "title": "Bmw", "text": "Спортивный характер", "img": "bmw.webp"},
    {"id": 3, "title": "Mers", "text": "Статус и надежность", "img": "mers.webp"},   
]

@app.get("/cars")
def get_cars():
    return cars_db

@app.get("/cars/{car_id}")
def get_car(car_id: int):
    for car in cars_db:
        if car["id"] == car_id:
            return car
    raise HTTPException(status_code = 404, detail = "Car not found")