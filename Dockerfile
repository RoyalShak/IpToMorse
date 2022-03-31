FROM ubuntu:20.04
RUN apt-get update
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN apt install python-is-python3
RUN apt-get install vim -y
WORKDIR /iptomorse
COPY req.txt .
RUN pip install --upgrade pip && pip install -r req.txt
COPY Ip-To-Morse-App.py /iptomorse
COPY connections.txt /iptomorse
CMD ["python", "-u", "Ip-To-Morse-App.py"]