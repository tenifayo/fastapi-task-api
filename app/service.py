from app.models import Task

class TaskService:
    def __init__(self):
        self.tasks = {}
        self.counter = 1

    def create_task(self, title, description, priority):
        task = Task(
            id=self.counter,
            title=title,
            description=description,
            priority=priority,
        )
        self.tasks[self.counter] = task
        self.counter += 1
        return task

    def get_tasks(self):
        return list(self.tasks.values())

    def update_task(self, task_id, data):
        task = self.tasks.get(task_id)
        if not task:
            return None

        for key, value in data.items():
            if value is not None:
                setattr(task, key, value)

        return task

    def delete_task(self, task_id):
        return self.tasks.pop(task_id, None)
