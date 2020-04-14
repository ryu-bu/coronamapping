FROM python:3

MAINTAINER Ryuichi Ohhata ryu74@bu.edu

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
