FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./src/model/ /code/

ENV GOOGLE_APPLICATION_CREDENTIALS=/code/speech-key.json

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
