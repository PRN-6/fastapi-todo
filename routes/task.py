from fastapi import APIRouter,HTTPException
from schemas.task import Task

router = APIRouter()

tasks = []

@router.post("/tasks")
def create_task(task: Task):
    tasks.append(task)
    return task

@router.get("/alltasks")
def get_tasks():
    return tasks

@router.get("/task/{id}")
def get_specific_task(id: int):
    for i in tasks:
        if i.id == id:
            return i
    raise HTTPException(status_code=404, detail="Task not found")

@router.put("/update/{id}")
def update_task(id: int, updated_task: Task):
    for i in tasks:
        if i.id == id:
            i.title = updated_task.title
            i.description = updated_task.description
            i.completed = updated_task.completed
            return i
    raise HTTPException(status_code=404, detail="Task not found")