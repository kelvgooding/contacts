FROM ubuntu:20.04
WORKDIR /app
COPY . /app
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y python3-mysql.connector
RUN pip3 install -r requirements.txt
EXPOSE 3003
CMD python3 ./app.py
