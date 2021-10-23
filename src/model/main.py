from google.cloud import speech
import io
import spacy
from fastapi import FastAPI

def transcribe_file(speech_file):

    client = speech.SpeechClient()

    with io.open(speech_file, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        audio_channel_count=2,
        sample_rate_hertz=48000,
        language_code="en-US",
    )

    response = client.recognize(config=config, audio=audio)

    sentence = ""

    for result in response.results:
        sentence = format(result.alternatives[0].transcript)

    return sentence

def tokenize(filePath): 
    sentence = transcribe_file(filePath)

    nlp = spacy.load("en_core_web_sm")
    doc = nlp(sentence)
    token = []
    for t in doc:
        if t.text[0] == "\'":
            token[-1] = token[-1] + t.text.lower()
        else:
            token.append(t.text.lower())

    return ' '.join(token)

app = FastAPI()

@app.get("/")
async def read_root():
    return "Please enter a file name."

@app.get("/{fileName}")
async def read_item(fileName):
    phrase = tokenize("src/model/" + str(fileName))
    return phrase

@app.get("/file/{fileName}")
async def read_item(fileName):
    phrase = tokenize(str(fileName))
    return phrase