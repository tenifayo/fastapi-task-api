from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import Base, engine
from app import models
from app.deps import get_db

app = FastAPI()


Base.metadata.create_all(bind=engine)


@app.post("/tasks")
def create_task(title: str, description: str = None, priority: int = 1, db: Session = Depends(get_db)):
    task = models.Task(
        title=title,
        description=description,
        priority=priority
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    return db.query(models.Task).all()


@app.patch("/tasks/{task_id}")
def update_task(task_id: int, completed: bool, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    task.completed = completed
    db.commit()
    return task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()

    return {"message": "deleted"}
