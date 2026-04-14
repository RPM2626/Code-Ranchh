from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from app.services.game_service import evaluate_guess

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

# Temporary in-memory storage
secret_number = "1234"  # you can replace with daily logic later


@router.get("/game")
def game_page(request: Request):
    return templates.TemplateResponse(
        request,
        "game.html",
        {"request": request}
    )


@router.post("/game")
async def submit_guess(request: Request):
    form = await request.form()
    guess = form.get("guess")

    # validation
    if not guess or len(guess) != 4 or not guess.isdigit():
        return templates.TemplateResponse(
            request,
            "game.html",
            {"request": request, "error": "Enter a valid 4-digit number"}
        )

    result = evaluate_guess(secret_number, guess)

    # FIXED: use object property instead of dict
    if result.bulls == 4:
        return RedirectResponse("/win", status_code=303)

    return templates.TemplateResponse(
        request,
        "game.html",
        {
            "request": request,
            "bulls": result.bulls,
            "cows": result.cows,
            "guess": guess
        }
    )


@router.get("/win")
def win_page(request: Request):
    return templates.TemplateResponse(
        request,
        "win.html",
        {"request": request}
    )
