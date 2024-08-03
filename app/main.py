import os
from fastapi import FastAPI
import uvicorn
from typing import Optional
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/hello")
def hello_page():
    return {"message": "Hello"}



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=82)
