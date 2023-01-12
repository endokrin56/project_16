import time
from celery import shared_task

@shared_task
def text():
    # time.sleep(1)
    print("Hello!")

@shared_task
def hello():
    time.sleep(10)
    print("Hello, world!")

@shared_task
def printer(N):
    for i in range(N):
        time.sleep(10)
        print(i+1)