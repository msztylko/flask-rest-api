FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

# Initialize new database
RUN ["python", "initial_db.py"]

CMD [ "python3", "api.py"]
