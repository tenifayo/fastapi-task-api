from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import Base, engine
from app import models
from app.deps import get_db
from app.schemas import TaskCreate, TaskUpdate

app = FastAPI()


Base.metadata.create_all(bind=engine)


@app.post("/tasks")
def create_task(task_in: TaskCreate, db: Session = Depends(get_db)):
    task = models.TaskModel(
        title=task_in.title,
        description=task_in.description,
        priority=task_in.priority
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    return db.query(models.TaskModel).all()


@app.patch("/tasks/{task_id}")
def update_task(
    task_id: int,
    task_in: TaskUpdate,
    db: Session = Depends(get_db)
):
    task = db.query(models.TaskModel).filter(
        models.TaskModel.id == task_id
    ).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if task_in.title is not None:
        task.title = task_in.title
    if task_in.description is not None:
        task.description = task_in.description
    if task_in.completed is not None:
        task.completed = task_in.completed
    if task_in.priority is not None:
        task.priority = task_in.priority

    db.commit()
    db.refresh(task)
    return task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.TaskModel).filter(
        models.TaskModel.id == task_id
    ).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()

    return {"message": "deleted"}
