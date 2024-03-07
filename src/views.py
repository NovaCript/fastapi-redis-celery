from fastapi import APIRouter
from tasks import vasya
from celery.result import AsyncResult

router = APIRouter()

@router.post('/add/')
async def add_task(x: int, y: int):
    task = vasya.send_task('tasks.add', args=[x, y])
    return {'task_id': str(task.id)}

@router.get('/tasks/{task_id}')
async def get_task_result(task_id: str):
    task = AsyncResult(task_id, app=vasya)
    if task.state == "SUCCESS":
        return {'task_id': task_id, 'status': task.state, 'result': task.result}
    return {'task_id': task_id, 'status': task.state}