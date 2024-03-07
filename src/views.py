from fastapi import APIRouter
from tasks import get_task_result, send_task

router = APIRouter()

@router.post('/add/')
async def add_task(x: int, y: int):
    return await send_task(x,y)

@app.get('/tasks/{task_id}')
async def get_task(task_id: str):
    return await get_task_result(task_id)
