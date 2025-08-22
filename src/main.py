from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.web import admin_routes, routes

app = FastAPI()

app.include_router(routes.router)
app.include_router(admin_routes.router)
app.mount("/static", StaticFiles(directory="static"), name="static")
