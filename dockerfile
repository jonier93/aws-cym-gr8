FROM python:latest

WORKDIR /project

COPY . /project

RUN pip install -r requirements.txt

CMD ["python", "server.py"]