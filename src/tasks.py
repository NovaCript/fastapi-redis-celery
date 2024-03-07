from celery import Celery
vasya = Celery('tasks', broker='redis://localhost:6379/0',backend='redis://localhost:6379/0')
vasya.config_from_object('celeryconfig')

@vasya.task
def add(x,y):
    return x+y