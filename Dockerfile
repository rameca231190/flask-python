FROM ubuntu:18.04
RUN apt-get update -y && \
    apt-get install -y software-properties-common && \
    add-apt-repository -y ppa:deadsnakes/ppa && \
    apt-get update -y && \
    apt-get install -y python3.8 python3-pip


RUN /usr/bin/python3 -m pip install --upgrade pip
RUN mkdir -p /app
WORKDIR /app
COPY ./app /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt
RUN adduser --uid 10001 --disabled-password --gecos ""  --shell /bin/bash --home /home/oms oms
RUN chown -R oms:oms /app
RUN chmod 755 /app
USER oms
EXPOSE 5000
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]
