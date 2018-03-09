FROM python:3.6-jessie

COPY requirements.txt ./
RUN pip install -r requirements.txt

# https://stackoverflow.com/questions/26822067/running-cron-python-jobs-within-docker

ADD . /work
WORKDIR /work

COPY test.py .
CMD ["python", "./test.py"]
