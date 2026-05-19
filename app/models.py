from dataclasses import dataclass
from typing import Optional

@dataclass
class Task:
    id: int
    title: str
    description: Optional[str]
    completed: bool = False
    priority: int = 1  # 1 = low, 2 = medium, 3 = high
