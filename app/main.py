from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import game, auth, history

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(auth.router)
app.include_router(game.router)
app.include_router(history.router)
