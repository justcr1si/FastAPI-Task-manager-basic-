from typing import Annotated

from fastapi import APIRouter, Depends

from repository import TaskRepository
from schemas import TaskAdd, Task

task_router = APIRouter(prefix='/tasks')


@task_router.post('')
async def add_task(
        task: Annotated[TaskAdd, Depends()]
) -> dict[str, bool | int]:
    task_id = await TaskRepository.add_one(task)
    return {'ok': True, 'task_id': task_id}


@task_router.get('')
async def get_tasks() -> dict[str, list[Task]]:
    tasks = await TaskRepository.find_all()
    return {'data': tasks}
