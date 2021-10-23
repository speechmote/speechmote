from fastapi import FastAPI
from src.model import main

app = FastAPI()

@app.get("/")
async def read_root():
    return "Please enter a file name."

@app.get("/{fileName}")
async def read_item(fileName):
    phrase = main.tokenize("src/model/" + str(fileName))
    return phrase

@app.get("/file/{fileName}")
async def read_item(fileName):
    phrase = main.tokenize(str(fileName))
    return phrase