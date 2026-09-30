from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from .database import init_db
from .routes import router


BASE_DIR = Path(__file__).resolve().parent

TEMPLATE_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"


app = FastAPI(
    title="FitBuddy – AI Fitness Plan Generator",
    version="1.0.0"
)


app.mount(
    "/static",
    StaticFiles(directory=STATIC_DIR),
    name="static"
)


templates = Jinja2Templates(
    directory=TEMPLATE_DIR
)


app.include_router(router)


@app.on_event("startup")
def startup():
    init_db()


@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "fitbuddy"
    }
@app.get("/", response_class=HTMLResponse)
def home():
    with open("app/templates/index.html", "r", encoding="utf-8") as f:
        return f.read()