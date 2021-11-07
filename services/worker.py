#from Celery import app_celery
import requests

#@app_celery.task(name='req')
def worker():
    new =  requests.post('https://gttb.guane.dev/api/workers?task_complexity=5')
    return new
