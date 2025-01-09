FROM python:3

USER root

ENV PYTHONUNBUFFERED=1
ENV PYTHONWRITEBYTECODE=1

WORKDIR /backend

COPY . /backend/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN apt-get update \
    && apt-get install -y libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

RUN chmod +x ./entrypoint-web.sh