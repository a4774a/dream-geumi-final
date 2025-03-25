from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from gpt_request import ask_gpt_dream

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def form_get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/interpret", response_class=HTMLResponse)
async def form_post(request: Request, dream: str = Form(...)):
    result = ask_gpt_dream(dream)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "dream": dream,
        "result": result
    })

