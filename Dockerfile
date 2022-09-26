# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ARG DJANGO_SECRET_KEY
WORKDIR /code
COPY requirements.txt /code/
COPY manage.py /code/
RUN pip install -r requirements.txt
COPY ./core /code/core
COPY ./pcs /code/pcs
COPY ./media /code/media
COPY ./static /code/static
COPY ./templates /code/templates
RUN python manage.py collectstatic --no-input
