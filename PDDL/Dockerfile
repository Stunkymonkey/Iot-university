# docker build .

FROM ubuntu:latest

RUN apt update
RUN apt install wget build-essential flex bison -y
RUN wget https://fai.cs.uni-saarland.de/hoffmann/ff/Metric-FF-v2.1.tgz
RUN tar xvf Metric-FF-v2.1.tgz
WORKDIR /Metric-FF-v2.1
RUN make
