FROM python:3.6-jessie

COPY requirements.txt ./
RUN pip install -r requirements.txt

ADD . /work
WORKDIR /work

COPY test.py .
RUN chmod a+x ./test.py

CMD ["python", "./pubtest.py"]
