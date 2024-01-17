# Author: Asif Iqbal Rahaman
# Start Date: 2023-12-16T12:30:00+05:30

from fastapi import FastAPI

app = FastAPI()

from src.web import routes
