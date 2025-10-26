from todolib import ToDoList


def display_menu():
    """Display the main menu"""
    print("\n" + "=" * 50)
    print("          TO-DO LIST MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Add New Task")
    print("2. View All Tasks")
    print("3. View Tasks by Filter")
    print("4. Mark Task as Completed")
    print("5. Delete Task")
    print("6. Show Statistics")
    print("7. Save and Exit")
    print("=" * 50)


def display_filter_menu():
    """Display filter options"""
    print("\nFilter Options:")
    print("1. All Tasks")
    print("2. Pending Tasks")
    print("3. Completed Tasks")
    print("4. High Priority")
    print("5. Medium Priority")
    print("6. Low Priority")


def get_priority_choice():
    """Get priority choice from user"""
    print("\nPriority Levels:")
    print("1. High")
    print("2. Medium")
    print("3. Low")

    while True:
        try:
            choice = int(input("Select priority (1-3): "))
            if choice == 1:
                return "High"
            elif choice == 2:
                return "Medium"
            elif choice == 3:
                return "Low"
            else:
                print("Please enter a number between 1 and 3")
        except ValueError:
            print("Please enter a valid number")


def main():
    todo_list = ToDoList("final_project/todo_list.csv")

    while True:
        display_menu()

        try:
            choice = int(input("\nEnter your choice (1-7): "))

            if choice == 1:
                # Add new task
                print("\nAdd New Task")
                name = input("Enter task name: ").strip()
                if not name:
                    print("Task name cannot be empty!")
                    continue

                description = input("Enter task description (optional): ").strip()
                priority = get_priority_choice()

                todo_list.add_task(name, description, priority)

            elif choice == 2:
                # View all tasks
                todo_list.view_tasks("All")

            elif choice == 3:
                # View tasks with filter
                display_filter_menu()
                try:
                    filter_choice = int(input("Select filter (1-6): "))
                    filters = {
                        1: "All",
                        2: "Pending",
                        3: "Completed",
                        4: "High",
                        5: "Medium",
                        6: "Low",
                    }
                    if filter_choice in filters:
                        todo_list.view_tasks(filters[filter_choice])
                    else:
                        print("Invalid filter choice!")
                except ValueError:
                    print("Please enter a valid number!")

            elif choice == 4:
                # Mark task as completed
                if not todo_list.tasks:
                    print("No tasks available!")
                    continue

                todo_list.view_tasks("Pending")
                try:
                    task_num = int(input("Enter task number to mark as completed: "))
                    todo_list.mark_task_completed(task_num - 1)
                except ValueError:
                    print("Please enter a valid number!")

            elif choice == 5:
                # Delete task
                if not todo_list.tasks:
                    print("No tasks available!")
                    continue

                todo_list.view_tasks("All")
                try:
                    task_num = int(input("Enter task number to delete: "))
                    todo_list.delete_task(task_num - 1)
                except ValueError:
                    print("Please enter a valid number!")

            elif choice == 6:
                # Show statistics
                stats = todo_list.get_task_count()
                print("\n" + "=" * 40)
                print("           TASK STATISTICS")
                print("=" * 40)
                print(f"Total Tasks: {stats['total']}")
                print(f"Completed: {stats['completed']}")
                print(f"Pending: {stats['pending']}")
                print(f"High Priority: {stats['high']}")
                print(f"Medium Priority: {stats['medium']}")
                print(f"Low Priority: {stats['low']}")
                print("=" * 40)

            elif choice == 7:
                # Save and exit
                todo_list.save_to_csv()
                print("To-do list saved successfully! Goodbye!")
                break

            else:
                print("Invalid choice! Please enter a number between 1 and 7.")

        except ValueError:
            print("Please enter a valid number!")
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Saving data...")
            todo_list.save_to_csv()
            print("Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
