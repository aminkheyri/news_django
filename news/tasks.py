from celery import shared_task



@shared_task
def adding(x, y):
    return x + y