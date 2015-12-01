FROM python:3.4.3

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
ADD . .

ENTRYPOINT ["python3", "main.py"]
