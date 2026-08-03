from fastapi import FastAPI
from sensors import *
from fastapi import Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

@app.get("/system")
def system():
    return {
        "cpu": {
            "temperature": cpu_temp(),
            "usage": cpu_usage()
        },
        "memory": {
            "usage": ram_usage()
        },
        "disk": {
            "usage": disk_usage()
        },
        "fan": {
            "rpm": fan_usage()

        }
    }
