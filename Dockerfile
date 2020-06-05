FROM python:3.8

LABEL maintainer = "ryu74@bu.edu"

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install requests

COPY . .

CMD gunicorn app:app --bind 0.0.0.0:$PORT --reload
