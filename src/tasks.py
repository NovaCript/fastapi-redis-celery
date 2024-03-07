from celery import Celery
celery = Celery('tasks', broker='redis://localhost:6379/0',backend='redis://localhost:6379/0')
celery.config_from_object('celeryconfig')

@celery.task
def add(x,y):
    return x+y



async def get_task_result(task_id: str):
    task = AsyncResult(task_id, app=celery)
    if task.state == "SUCCESS":
        return {'task_id': task_id, 'status': task.state, 'result': await task.get()}
    return {'task_id': task_id, 'status': task.state}


async def send_task(x:int, y:int):
    task = celery.send_task('tasks.add', args=[x, y])
    return {'task_id': str(task.id)}
