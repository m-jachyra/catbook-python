FROM python:3.10-alpine

WORKDIR /app

COPY ./backend/app/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./backend/app /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8888"]