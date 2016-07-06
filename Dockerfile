FROM python:2.7
ENV PYTHONBUFFERED 1
WORKDIR /welcome
RUN echo $(ls -la)
ADD requirements.txt /welcome/
RUN pip install -r requirements.txt
ADD . /welcome/
