import uvicorn
from fastapi import FastAPI

import pandas as pd
import cities, persons
import html_render

app = FastAPI()
app.include_router(cities.router)
app.include_router(persons.router)
app.include_router(html_render.router)


@app.get("/")
def get_root():
    return {"message": "hello"}


@app.get("/txt/{filename}")
def get_txt(filename: str):
    with open(filename, mode="r") as f:
        s = f.read()
    return {"text": s.split("\n")}


@app.get("/txt/{filename}/{row}")
def get_txt_row(filename: str, row: int):
    with open(filename, mode="r") as f:
        s = f.read()
    return {"text": s.split("\n")[row]}


@app.post("/post/")
def post_num(message: str):
    print(message)
    return {"message": message}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
