import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routers.game import router as game_router

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(game_router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
