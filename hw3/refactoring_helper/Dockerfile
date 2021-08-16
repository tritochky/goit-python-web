FROM python:3-slim-buster

WORKDIR /app

RUN pip install pipenv

COPY . /app

RUN pipenv install --system --deploy

CMD python /app/refactoring_helper/main.py
