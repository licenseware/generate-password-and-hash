FROM python:3.13-alpine

LABEL author="Meysam Azad <meysam@licenseware.io>"

ENV PYTHONUNBUFFERED=1

RUN apk add --update gcc musl-dev libffi-dev && pip install -U pip

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["/main.py"]
