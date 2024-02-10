FROM python:3.8-slim-buster

RUN apt update -y && apt install -y awscli

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app

CMD ["streamlit", "run", "app.py"]
