from software import app, templates
from fastapi import Request, Form

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# @app.post("/")
# async def test(cores_exclusivas: str):
#     return "test"

# @app.post("/")
# async def test():
#     return "test"

@app.post("/save_file")
async def test2():
    return 'test 2'

# @app.get("/save_file/{cores_exclusivas}")
# async def save_file(cores_exclusivas: str):
#     # with open('cores_exclusivas.txt', 'w') as arq:  # ruby, gray, blue, red, pink, purple
#     #     return arq.write(cores_exclusivas) > 0
#     return cores_exclusivas
""" @app.get("/save_file")
async def save_file(cores_exclusivas: str):
    # with open('cores_exclusivas.txt', 'w') as arq:  # ruby, gray, blue, red, pink, purple
    #     return arq.write(cores_exclusivas) > 0
    return cores_exclusivas """

# @app.post("/save_file")
# async def save_file(cores_exclusivas: str):
#     # with open('cores_exclusivas.txt', 'w') as arq:  # ruby, gray, blue, red, pink, purple
#     #     return arq.write(cores_exclusivas) > 0
#     return True

# @app.get("/save_file")
# async def save_file():
#     cores_exclusivas = "ruby, gray, blue, red, pink, purple"
#     with open('cores_exclusivas.txt', 'w') as arq:  # ruby, gray, blue, red, pink, purple
#         return arq.write(cores_exclusivas) > 0
#     return False