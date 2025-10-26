import csv
import os
from typing import List

from .task import Task


class ToDoList:
    def __init__(self, filename: str = "todo_list.csv"):
        self.filename = filename
        self.tasks: List[Task] = []
        self.load_from_csv()

    def add_task(self, name: str, description: str = "", priority: str = "Medium"):
        """Add a new task to the to-do list"""
        if priority not in ["High", "Medium", "Low"]:
            priority = "Medium"

        task = Task(name, description, priority)
        self.tasks.append(task)
        self.save_to_csv()
        print(f"Task '{name}' added successfully!")

    def delete_task(self, task_index: int):
        """Delete a task from the to-do list by index"""
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            self.save_to_csv()
            print(f"Task '{removed_task.name}' deleted successfully!")
        else:
            print("Invalid task index!")

    def mark_task_completed(self, task_index: int):
        """Mark a task as completed"""
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_completed()
            self.save_to_csv()
            print(f"Task '{self.tasks[task_index].name}' marked as completed!")
        else:
            print("Invalid task index!")

    def view_tasks(self, filter_type: str = "All"):
        """Display all tasks with optional filtering"""
        if not self.tasks:
            print("No tasks in the to-do list!")
            return

        print(f"\n{'='*60}")
        print(f"TO-DO LIST ({filter_type} Tasks)")
        print(f"{'='*60}")

        filtered_tasks = self.tasks

        if filter_type == "Completed":
            filtered_tasks = [task for task in self.tasks if task.completed]
        elif filter_type == "Pending":
            filtered_tasks = [task for task in self.tasks if not task.completed]
        elif filter_type == "High":
            filtered_tasks = [task for task in self.tasks if task.priority == "High"]
        elif filter_type == "Medium":
            filtered_tasks = [task for task in self.tasks if task.priority == "Medium"]
        elif filter_type == "Low":
            filtered_tasks = [task for task in self.tasks if task.priority == "Low"]

        if not filtered_tasks:
            print(f"No {filter_type.lower()} tasks found!")
            return

        for i, task in enumerate(filtered_tasks):
            print(f"{i+1}. {task}")
            if task.description:
                print(f"   Description: {task.description}")
            print()

    def save_to_csv(self):
        """Save all tasks to a CSV file"""
        try:
            with open(self.filename, "w", newline="", encoding="utf-8") as file:
                if self.tasks:
                    fieldnames = [
                        "name",
                        "description",
                        "priority",
                        "created_date",
                        "completed",
                    ]
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    for task in self.tasks:
                        writer.writerow(task.to_dict())
        except Exception as e:
            print(f"Error saving to CSV: {e}")

    def load_from_csv(self):
        """Load tasks from a CSV file"""
        if not os.path.exists(self.filename):
            return

        try:
            with open(self.filename, "r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                self.tasks.clear()
                for row in reader:
                    task = Task.from_dict(row)
                    self.tasks.append(task)
        except Exception as e:
            print(f"Error loading from CSV: {e}")

    def get_task_count(self):
        """Get statistics about tasks"""
        total = len(self.tasks)
        completed = sum(1 for task in self.tasks if task.completed)
        pending = total - completed

        high_priority = sum(1 for task in self.tasks if task.priority == "High")
        medium_priority = sum(1 for task in self.tasks if task.priority == "Medium")
        low_priority = sum(1 for task in self.tasks if task.priority == "Low")

        return {
            "total": total,
            "completed": completed,
            "pending": pending,
            "high": high_priority,
            "medium": medium_priority,
            "low": low_priority,
        }
