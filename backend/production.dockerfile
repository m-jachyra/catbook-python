FROM python:3.10-alpine

WORKDIR /app

COPY ./backend/app/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./backend/app /app

EXPOSE 8000

CMD ["sh", "start.sh"]