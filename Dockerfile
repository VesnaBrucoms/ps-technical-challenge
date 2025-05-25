FROM python:3.11.12-alpine

COPY . /tmp/challenge
RUN pip install /tmp/challenge

CMD flask run --host=0.0.0.0