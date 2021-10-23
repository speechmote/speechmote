from fastapi import FastAPI
import model

app = FastAPI()

@app.get("/")
async def read_root():
    return "Please enter a file name."

@app.get("/file/{fileName}")
async def read_item(fileName):
    phrase = model.tokenize("/code/" + str(fileName))
    return phrase

@app.get("/test/{item_id}")
async def test_read(item_id: str):
    return "recieved" + item_id
