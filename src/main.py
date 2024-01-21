# Author: Asif Iqbal Rahaman
# Start Date: 2023-12-16T12:30:00+05:30

# import uvicorn
from fastapi import FastAPI

app = FastAPI()

from src.web import routes

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)
