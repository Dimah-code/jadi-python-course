from datetime import datetime


class Task:
    def __init__(self, name: str, description: str = "", priority: str = "Medium"):
        self.name = name
        self.description = description
        self.priority = priority
        self.created_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.name} | Priority: {self.priority} | Created: {self.created_date}"

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "priority": self.priority,
            "created_date": self.created_date,
            "completed": str(self.completed),
        }

    @classmethod
    def from_dict(cls, data: dict):
        task = cls(data["name"], data["description"], data["priority"])
        task.created_date = data["created_date"]
        task.completed = data["completed"].lower() == "true"
        return task
