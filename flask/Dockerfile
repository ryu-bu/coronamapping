FROM python:3.8

LABEL maintainer = "ryu74@bu.edu"

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uwsgi", "app.ini"]
