FROM python:3.6-jessie

COPY requirements.txt ./
RUN pip install -r requirements.txt

# https://stackoverflow.com/questions/26822067/running-cron-python-jobs-within-docker
# https://stackoverflow.com/questions/47758657/how-can-i-run-cron-in-docker-no-jobs-output-even-with-simple-crontab

ADD . /work
WORKDIR /work

COPY test.py .
RUN chmod a+x ./test.py


CMD ["python", "./test.py"]
#RUN crontab ./testcrontab
#ENTRYPOINT cron -f
