FROM ghcr.io/joda-explore/joda/joda:latest

# Install python dependencies
COPY modules/requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Download model
RUN mkdir -p /model
RUN apt-get update &&  apt-get install -y wget && rm -rf /var/lib/apt/lists/*
RUN wget -O /model/lid.176.ftz https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.ftz