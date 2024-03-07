from celery import Celery
vasya = Celery('tasks', broker='redis://localhost:6379/0',backend='redis://localhost:6379/0')
vasya.config_from_object('celeryconfig')

@vasya.task
def add(x,y):
    return x+y



async def get_task_result(task_id: str):
    task = AsyncResult(task_id, app=vasya)
    if task.state == "SUCCESS":
        return {'task_id': task_id, 'status': task.state, 'result': await task.get()}
    return {'task_id': task_id, 'status': task.state}
