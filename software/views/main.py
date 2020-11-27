from software import app, templates
from fastapi import Request

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/save_file")
async def save_file(cores_exclusivas: str):
    with open('cores_exclusivas.txt', 'w') as arq:  # ruby, gray, blue, red, pink, purple
        return arq.write(cores_exclusivas) > 0
    return True