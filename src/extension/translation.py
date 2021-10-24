from google.cloud import speech_v1p1beta1
import requests
import io
import json

def transcribe_file(speech_file):

    client = speech_v1p1beta1.SpeechClient()

    with io.open(speech_file, "rb") as audio_file:
        content = audio_file.read()

    audio = speech_v1p1beta1.RecognitionAudio(content=content)
    config = speech_v1p1beta1.RecognitionConfig(
        encoding=speech_v1p1beta1.RecognitionConfig.AudioEncoding.WEBM_OPUS,
        audio_channel_count=2,
        sample_rate_hertz=48000,
        language_code="en-US",
    )

    response = client.recognize(config=config, audio=audio)

    sentence = ""

    for result in response.results:
        sentence = format(result.alternatives[0].transcript)

    return sentence

url = "https://speechmote-329915.ue.r.appspot.com/process/"
string = transcribe_file("src/extension/sample.webm") # add file path

response = requests.get(url + string)

f = open("resultingVal.txt", "a")
f.write(response.json())
f.close()