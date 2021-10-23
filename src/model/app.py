from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import model
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:8080",
    "https://speechmote-329915.ue.r.appspot.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return "Please enter a file name."

@app.get("/file/{fileName}")
async def read_item(fileName):
    phrase = model.tokenize("/code/" + str(fileName))
    return phrase

@app.get("/test/{item_id}")
async def test_read(item_id: str):
    return {"recieved:" + item_id}
