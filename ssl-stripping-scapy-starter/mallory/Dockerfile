FROM ubuntu:latest

RUN apt-get update && apt-get install python python3 python3-pip python-dev libdnet iptables net-tools nano git -y

Run pip3 install --upgrade pip
RUN pip3 install netifaces 
RUN pip3 install scapy-python3
RUN git clone https://github.com/invernizzi/scapy-http.git && \
    cd scapy-http && \
    python3 setup.py install && \ 
    apt-get remove -y git && \
    rm -rf /scapy-http