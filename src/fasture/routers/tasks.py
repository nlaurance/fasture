from fastapi import APIRouter, HTTPException
from fasture import schemas
from fasture import task_db

router = APIRouter()


@router.get(
    "/{task_id}",
    summary="Get info about a task",
    response_model=schemas.Task,
)
async def get_specific_task(task_id: str) -> schemas.Task:
    future_task = task_db.get_task_by_id(task_id)
    if future_task is None:
        raise HTTPException(status_code=404, detail="Item not found")
    task = schemas.Task(
        uid=future_task.uid,
        job_name=future_task.job_name,
        created_at=future_task.created_at,
        completed_at=future_task.completed_at,
        state=future_task.state,
        result=future_task.result,
    )
    return task


@router.delete(
    "/{task_id}",
    summary="Cancels a task",
    response_model=schemas.Task,
)
async def get_specific_task(task_id: str) -> schemas.Task:
    future_task = task_db.get_task_by_id(task_id)
    if future_task is None:
        raise HTTPException(status_code=404, detail="Item not found")
    future_task.future.cancel()
    task = schemas.Task(
        uid=future_task.uid,
        job_name=future_task.job_name,
        created_at=future_task.created_at,
        completed_at=future_task.completed_at,
        state=future_task.state,
        result=future_task.result,
    )
    return task
