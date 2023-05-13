FROM python:3.11

ENV DockerHOME=/app
RUN mkdir -p $DockerHOME
WORKDIR $DockerHOME

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY requirements.txt $DockerHOME
RUN pip install -r requirements.txt

COPY . $DockerHOME

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000