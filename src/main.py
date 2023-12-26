# Author: Asif Iqbal Rahaman
# Start Date: 2023-12-16T12:30:00+05:30

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/profile", name="profile", response_class=HTMLResponse)
def read_profile(request: Request):
    return templates.TemplateResponse("profile.html", {"request": request})


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
