FROM python:3.10

WORKDIR /app

COPY ./backend/app/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./backend/app /app

EXPOSE 3100

CMD ["gunicorn", "main:app"]