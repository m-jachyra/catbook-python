FROM python:3.10-alpine

RUN mkdir -p /app
RUN echo ${PWD} && ls -lR

WORKDIR /app

RUN echo ${PWD} && ls -lR
COPY ./app/requirements.txt /app/requirements.txt

RUN echo ${PWD} && ls -lR
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

RUN echo ${PWD} && ls -lR
COPY ./app /app

RUN echo ${PWD} && ls -lR

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8888"]