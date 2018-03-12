FROM python:3.6-jessie

COPY requirements.txt ./
RUN pip install -r requirements.txt

ADD . /work
WORKDIR /work

COPY pubtest.py .
RUN chmod a+x ./pubtest.py

CMD ["python", "./pubtest.py"]
