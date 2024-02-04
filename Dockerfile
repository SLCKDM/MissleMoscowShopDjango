FROM python:3

USER root

ENV PYTHONUNBUFFERED=1
ENV PYTHONWRITEBYTECODE=1

WORKDIR /backend

COPY . /backend/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN chmod +x ./entrypoint-web.sh
RUN chmod +x ./entrypoint-web-test.sh