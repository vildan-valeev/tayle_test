FROM python:3.8

ENV PYTHONUNBUFFERED 1
#  рабочая директория
WORKDIR /app

#  установка бибилиотек
COPY ./pyproject.toml ./poetry.lock ./app/start.sh /

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

