FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./src/model /code/app

ENV GOOGLE_APPLICATION_CREDENTIALS=src/model/speech-key.json

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]