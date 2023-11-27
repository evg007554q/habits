FROM python:3

WORKDIR /habits

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .
