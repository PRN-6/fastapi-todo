from fastapi import APIRouter, HTTPException, status
from schemas.task import TaskCreate, TaskUpdate, TaskResponse
from typing import List

router = APIRouter(prefix="/tasks", tags=["Tasks"])

# In-memory store: list of dicts (simulates a DB until we add SQLAlchemy)
tasks: list[dict] = []
_id_counter = 1  # Auto-increment ID simulation


@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    global _id_counter
    new_task = task.model_dump()
    new_task["id"] = _id_counter
    _id_counter += 1
    tasks.append(new_task)
    return new_task


@router.get("/", response_model=List[TaskResponse])
def get_all_tasks():
    return tasks


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")


@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, updated_task: TaskCreate):
    for task in tasks:
        if task["id"] == task_id:
            task.update(updated_task.model_dump())
            return task
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")


@router.patch("/{task_id}", response_model=TaskResponse)
def partial_update_task(task_id: int, updated_task: TaskUpdate):
    for task in tasks:
        if task["id"] == task_id:
            # Only update fields that were explicitly provided (not None)
            patch_data = updated_task.model_dump(exclude_unset=True)
            task.update(patch_data)
            return task
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(index)
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")