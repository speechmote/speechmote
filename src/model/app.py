from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import model

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


@app.get("/process/{to_process}")
async def process_text(to_process):
    return model.tokenize(to_process)
