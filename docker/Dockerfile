FROM python:3.8-slim-buster

RUN apt-get update \
    && apt-get install -y gcc

WORKDIR /app
COPY requirements.txt .
COPY /app/. .
RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
