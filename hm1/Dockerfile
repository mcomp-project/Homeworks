FROM python:3.10

RUN mkdir /work
COPY . /work

WORKDIR /work

RUN pip install --upgrade pip
RUN pip install numpy

ENTRYPOINT ["python","main.py"]
CMD ["cat","main.py"]
