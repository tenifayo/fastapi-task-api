from dataclasses import dataclass
from typing import Optional
from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base


@dataclass
class Task:
    id: int
    title: str
    description: Optional[str]
    completed: bool = False
    priority: int = 1  # 1 = low, 2 = medium, 3 = high


class TaskModel(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    completed = Column(Boolean, default=False)
    priority = Column(Integer, default=1)
