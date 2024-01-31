#!/bin/bash

# Run alembic migrations
alembic upgrade head

# Start server
gunicorn -k uvicorn.workers.UvicornWorker -b :8000 main:app
