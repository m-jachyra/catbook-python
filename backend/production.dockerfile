FROM python:3.10

WORKDIR /app

COPY ./backend/app/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./backend/app /app

RUN alembic upgrade head

EXPOSE 8000

CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-b", ":8000", "main:app"]