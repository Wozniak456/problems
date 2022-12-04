FROM python:3.6-slim

ENV FLASK_APP=back_rep1_main

ENV FLASK_DEBUG=$FLASK_DEBUG

COPY requirements.txt /opt

RUN python3 -m pip install -r /opt/requirements.txt

COPY back_rep1_main /opt/back_rep1_main

WORKDIR /opt

CMD flask run --host 0.0.0.0 -p $PORT
