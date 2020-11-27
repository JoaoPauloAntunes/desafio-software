from software import app, templates
from fastapi import Request

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/save_file")
async def save_file(exclusive_colors: str):
    with open('exclusive_colors.txt', 'w') as arq:
        return arq.write(exclusive_colors) > 0
    return False