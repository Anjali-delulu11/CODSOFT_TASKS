import json
from datetime import datetime

FILE_NAME = "tasks.json"


# ---------------- LOAD & SAVE TASKS ----------------

def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


tasks = load_tasks()


# ---------------- DISPLAY TASKS ----------------

def show_tasks(task_list=None):
    if task_list is None:
        task_list = tasks

    if not task_list:
        print("\n📭 No tasks found.")
        return

    print("\n" + "=" * 75)
    print("                         📋 YOUR TASKS")
    print("=" * 75)

    for index, task in enumerate(task_list, start=1):
        status = "✅ Done" if task["completed"] else "⏳ Pending"

        print(f"""
{index}. {task["title"]}
   📌 Category : {task["category"]}
   🔥 Priority : {task["priority"]}
   📅 Due Date : {task["due_date"]}
   📊 Status   : {status}
""")


# ---------------- ADD TASK ----------------

def add_task():
    print("\n➕ ADD NEW TASK")

    title = input("Enter task: ").strip()

    if not title:
        print("❌ Task cannot be empty.")
        return

    print("\nCategories:")
    print("1. 📚 Study")
    print("2. 💼 Work")
    print("3. 🏠 Personal")
    print("4. 🌟 Other")

    category_choice = input("Choose category: ")

    categories = {
        "1": "Study",
        "2": "Work",
        "3": "Personal",
        "4": "Other"
    }

    category = categories.get(category_choice, "Other")

    print("\nPriority:")
    print("1. 🔴 High")
    print("2. 🟡 Medium")
    print("3. 🟢 Low")

    priority_choice = input("Choose priority: ")

    priorities = {
        "1": "High",
        "2": "Medium",
        "3": "Low"
    }

    priority = priorities.get(priority_choice, "Medium")

    due_date = input("\nEnter due date (DD-MM-YYYY): ").strip()

    # Validate date
    try:
        datetime.strptime(due_date, "%d-%m-%Y")
    except ValueError:
        print("❌ Invalid date. Task was not added.")
        return

    new_task = {
        "title": title,
        "category": category,
        "priority": priority,
        "due_date": due_date,
        "completed": False
    }

    tasks.append(new_task)
    save_tasks()

    print("\n🎉 Task added successfully!")


# ---------------- COMPLETE TASK ----------------

def complete_task():
    show_tasks()

    if not tasks:
        return

    try:
        number = int(input("\nEnter task number to complete: "))

        if 1 <= number <= len(tasks):

            if tasks[number - 1]["completed"]:
                print("ℹ️ Task is already completed.")
            else:
                tasks[number - 1]["completed"] = True
                save_tasks()
                print("🎉 Task completed!")

        else:
            print("❌ Invalid task number.")

    except ValueError:
        print("❌ Please enter a valid number.")


# ---------------- DELETE TASK ----------------

def delete_task():
    show_tasks()

    if not tasks:
        return

    try:
        number = int(input("\nEnter task number to delete: "))

        if 1 <= number <= len(tasks):
            deleted = tasks.pop(number - 1)
            save_tasks()

            print(f"🗑️ '{deleted['title']}' deleted successfully!")

        else:
            print("❌ Invalid task number.")

    except ValueError:
        print("❌ Please enter a valid number.")


# ---------------- UPDATE TASK ----------------

def update_task():
    show_tasks()

    if not tasks:
        return

    try:
        number = int(input("\nEnter task number to update: "))

        if not (1 <= number <= len(tasks)):
            print("❌ Invalid task number.")
            return

        task = tasks[number - 1]

        print("\nLeave blank if you don't want to change something.")

        new_title = input(f"New title [{task['title']}]: ").strip()

        if new_title:
            task["title"] = new_title

        new_date = input(f"New due date [{task['due_date']}]: ").strip()

        if new_date:
            try:
                datetime.strptime(new_date, "%d-%m-%Y")
                task["due_date"] = new_date
            except ValueError:
                print("❌ Invalid date. Old date kept.")

        save_tasks()

        print("✅ Task updated successfully!")

    except ValueError:
        print("❌ Please enter a valid number.")


# ---------------- SEARCH TASK ----------------

def search_task():
    keyword = input("\n🔍 Enter keyword to search: ").lower().strip()

    results = [
        task for task in tasks
        if keyword in task["title"].lower()
        or keyword in task["category"].lower()
        or keyword in task["priority"].lower()
    ]

    if results:
        print(f"\n🔎 Found {len(results)} task(s):")
        show_tasks(results)
    else:
        print("❌ No matching tasks found.")


# ---------------- PROGRESS ----------------

def show_progress():
    total = len(tasks)

    if total == 0:
        print("\n📊 No tasks available.")
        return

    completed = sum(task["completed"] for task in tasks)
    pending = total - completed

    percentage = int((completed / total) * 100)

    bars = int(percentage / 10)
    progress_bar = "█" * bars + "░" * (10 - bars)

    print("\n" + "=" * 50)
    print("                 📊 PROGRESS")
    print("=" * 50)

    print(f"Total Tasks     : {total}")
    print(f"Completed       : {completed}")
    print(f"Pending         : {pending}")
    print(f"Progress        : {percentage}%")
    print(f"[{progress_bar}]")

    print("=" * 50)


# ---------------- MAIN MENU ----------------

while True:

    print("\n")
    print("=" * 55)
    print("              ✨ SMART TO-DO MANAGER ✨")
    print("=" * 55)

    print("1. ➕ Add Task")
    print("2. 📋 View Tasks")
    print("3. ✏️ Update Task")
    print("4. ✅ Complete Task")
    print("5. 🗑️ Delete Task")
    print("6. 🔍 Search Task")
    print("7. 📊 View Progress")
    print("8. 🚪 Exit")

    print("=" * 55)

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_task()

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        update_task()

    elif choice == "4":
        complete_task()

    elif choice == "5":
        delete_task()

    elif choice == "6":
        search_task()

    elif choice == "7":
        show_progress()

    elif choice == "8":
        print("\n👋 Thank you for using Smart To-Do Manager!")
        print("✨ Stay productive!")
        break

    else:
        print("\n❌ Invalid choice. Please select 1-8.")