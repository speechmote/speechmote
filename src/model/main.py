from google.cloud import speech
import io
import spacy
from fastapi import FastAPI

def transcribe_file(speech_file):
    """Transcribe the given audio file."""

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

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
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

    return token

app = FastAPI()

@app.get("/")
def read_root():
    return "Welcome to Speechmote"


@app.get("/{fileName}")
def read_item(fileName):
    array = tokenize("src/model/" + str(fileName))
    return array
