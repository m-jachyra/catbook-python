from celery import Celery

from config import settings


celery_app = Celery("worker", broker=settings.QUEUE_URL)
