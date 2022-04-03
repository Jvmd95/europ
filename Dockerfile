FROM rocker/r-apt:bionic
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends build-essential python3.8 python3-pip python3-setuptools python3-dev
RUN pip3 install --upgrade pip

ENV PYTHONPATH "${PYTHONPATH}:/app"
WORKDIR /app

COPY requirements.txt .

# installing python libraries
RUN pip3 install -r requirements.txt
RUN python -m pytest tests/


CMD [ "python3",  "europcar/main.py" ]