from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/login")
def login_page(request: Request):
    return templates.TemplateResponse(
        request,
        "login.html",
        {"request": request}
    )


@router.post("/login")
async def login(request: Request):
    form = await request.form()
    username = form.get("username")
    password = form.get("password")

    if username == "bob" and password == "bobpass":
        response = RedirectResponse(url="/game", status_code=303)
        response.set_cookie(key="user", value=username)
        return response

    return templates.TemplateResponse(
        request,
        "login.html",
        {"request": request, "error": "Invalid credentials"}
    )
