FROM python:3
RUN apt-get update -y && apt-get install -y build-essential
RUN pip3 install --upgrade pip

ENV PYTHONPATH "${PYTHONPATH}:/app"
WORKDIR /app

COPY requirements.txt .

# installing python libraries
RUN python3 -m pip install -r requirements.txt


CMD [ "python3",  "europcar\main.py" ]