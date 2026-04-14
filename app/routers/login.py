from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import Request, Form
from . import router, templates


@router.get("/login", response_class=HTMLResponse)
async def login_view(request: Request):
    return templates.TemplateResponse(
        "login.html",
        {"request": request, "error": None}
    )


@router.post("/login", response_class=HTMLResponse)
async def login_action(request: Request, username: str = Form(...), password: str = Form(...)):

    if username == "bob" and password == "bobpass":
        return RedirectResponse(url="/game", status_code=303)

    return templates.TemplateResponse(
        "login.html",
        {"request": request, "error": "Invalid username or password"}
    )
