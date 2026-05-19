from fastapi import FastAPI, HTTPException
from app.schemas import TaskCreate, TaskUpdate
from app.service import TaskService


app = FastAPI()
service = TaskService()


@app.get("/")
def root():
    return {"message": "Task API running"}


@app.post("/tasks")
def create_task(task: TaskCreate):
    return service.create_task(
        task.title,
        task.description,
        task.priority
    )


@app.get("/tasks")
def list_tasks():
    return service.get_tasks()


@app.patch("/tasks/{task_id}")
def update_task(task_id: int, task: TaskUpdate):
    updated = service.update_task(task_id, task.model_dump())
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    deleted = service.delete_task(task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Deleted"}
