FROM python:3.10-slim

WORKDIR /app


COPY log_script.py /app

CMD [ "python", "log_script.py" ]