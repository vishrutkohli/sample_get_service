#1.) build the docker image ----> docker build .
#2.) run the docker image ----> docker run -p 8000:8000 -v $(pwd):/app <IMAGE_ID>
FROM python:3.6-slim

RUN apt-get update && apt-get install -y git

COPY . /app/

WORKDIR /app/alerts

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "manage.py", "makemigrations"]
ENTRYPOINT ["python", "manage.py", "migrate"]
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]


