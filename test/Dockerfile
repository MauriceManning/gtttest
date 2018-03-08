FROM python:3.6
RUN pip install -r requirements.txt

ADD . /work
WORKDIR /work

COPY test.py .
CMD['python', 'test.py']
