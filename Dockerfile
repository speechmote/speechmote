FROM ubuntu:20.04
COPY . /src/model
CMD python /src/model/main.py