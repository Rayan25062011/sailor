FROM python:3.8

COPY scripts/ .

RUN pip install -r requirements.txt

CMD [ "python", "sailor.py"]
