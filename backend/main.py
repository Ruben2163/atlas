from fastapi import FastAPI
from stats import cpu_temp

app = FastAPI()

@app.get("/")
def home():
    return {"message": "PiHub API"}

@app.get("/temperature")
def get_temperature():
    return {
        "temperature": cpu_temp()
    }
