from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

router = APIRouter()
api_router = APIRouter()
templates = Jinja2Templates(directory="app/templates")
static_files = StaticFiles(directory="app/static")
