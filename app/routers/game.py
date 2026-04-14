from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from app.services.game_service import (
    evaluate_guess,
    get_history,
    reset_game,
    get_today,
    get_time_until_next_challenge,
)

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@router.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse(
        "login.html",
        {
            "request": request,
            "error": None
        }
    )


@router.post("/login", response_class=HTMLResponse)
def login_submit(
    request: Request,
    username: str = Form(...),
    password: str = Form(...)
):
    if username == "bob" and password == "bobpass":
        return RedirectResponse(url="/game", status_code=303)

    return templates.TemplateResponse(
        "login.html",
        {
            "request": request,
            "error": "Invalid username or password"
        }
    )


@router.get("/register", response_class=HTMLResponse)
def register_page(request: Request):
    return templates.TemplateResponse(
        "register.html",
        {"request": request}
    )


@router.get("/game", response_class=HTMLResponse)
def game_page(request: Request):
    return templates.TemplateResponse(
        "game.html",
        {
            "request": request,
            "history": get_history(),
            "today": get_today(),
            "timer": get_time_until_next_challenge(),
        }
    )


@router.post("/game", response_class=HTMLResponse)
def game_submit(
    request: Request,
    guess: str = Form(...)
):
    if len(guess) == 4 and guess.isdigit():
        result = evaluate_guess(guess)

        if result["bulls"] == 4:
            return RedirectResponse(url="/win", status_code=303)

    return RedirectResponse(url="/game", status_code=303)


@router.get("/win", response_class=HTMLResponse)
def win_page(request: Request):
    return templates.TemplateResponse(
        "win.html",
        {
            "request": request,
            "today": get_today(),
            "timer": get_time_until_next_challenge(),
        }
    )


@router.get("/history", response_class=HTMLResponse)
def history_page(request: Request):
    return templates.TemplateResponse(
        "history.html",
        {
            "request": request,
            "history": get_history(),
            "today": get_today(),
            "timer": get_time_until_next_challenge(),
        }
    )


@router.get("/reset")
def reset_daily_game():
    reset_game()
    return RedirectResponse(url="/game", status_code=303)
