FROM python:3.11.12-alpine

COPY . /tmp/ps-challenge
RUN pip install /tmp/ps-challenge/.

RUN rm -rf /tmp/ps-challenge

EXPOSE 5000

CMD ["flask", "--app", "ps_challenge.app", "run", "--host=0.0.0.0"]