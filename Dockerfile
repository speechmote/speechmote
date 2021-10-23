FROM python:3.9
COPY . /src/model

ENV GOOGLE_APPLICATION_CREDENTIALS=src/model/speech-key.json