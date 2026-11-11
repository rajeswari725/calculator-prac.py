# ----------------------------
# TODO List Program (with DEBUG)
# ----------------------------

# Initialize program state
# todo_list = []  # this stores all tasks as dicts
# task_id = 1     # unique ID for each task
# DEBUG = True    # set True to see raw data after each operation

# # Function to add a task
# def add_task():
#     global task_id
#     task_name = input("Enter task name: ").strip()
#     if not task_name:
#         print("Task cannot be empty.")
#         return

#     # Create a dict for the task
#     task = {"id": task_id, "name": task_name, "status": "pending"}
#     todo_list.append(task)
#     print(f"Task added: {task_name} with ID {task_id}")

#     # Increment task_id for next task
#     task_id += 1

#     # DEBUG: show current state of todo_list
#     if DEBUG:
#         print("DEBUG:", todo_list)


# # Function to view all tasks
# def view_tasks():
#     if not todo_list:
#         print("No tasks found.")
#         return

#     print("\nID   TASK NAME           STATUS")
#     print("-" * 35)
#     for task in todo_list:
#         print(f"{task['id']:<4} {task['name']:<20} {task['status']}")

#     # DEBUG: show raw data
#     if DEBUG:
#         print("DEBUG (raw data):", todo_list)


# # Function to update a task (mark as done)
# def update_task():
#     if not todo_list:
#         print("No tasks to update.")
#         return

#     try:
#         tid = int(input("Enter task ID to mark as done: "))
#     except ValueError:
#         print("Invalid input. Enter a number.")
#         return

#     # Search for task
#     for task in todo_list:
#         if task["id"] == tid:
#             if task["status"] == "Done":
#                 print("Task already marked as done.")
#             else:
#                 task["status"] = "Done"
#                 print(f"Task '{task['name']}' marked as done.")
#             break
#     else:
#         print("Task ID not found.")

#     if DEBUG:
#         print("DEBUG:", todo_list)


# # Function to delete a task
# def delete_task():
#     if not todo_list:
#         print("No tasks to delete.")
#         return

#     try:
#         tid = int(input("Enter task ID to delete: "))
#     except ValueError:
#         print("Invalid input. Enter a number.")
#         return

#     for i, task in enumerate(todo_list):
#         if task["id"] == tid:
#             removed = todo_list.pop(i)
#             print(f"Task '{removed['name']}' deleted.")
#             break
#     else:
#         print("Task ID not found.")

#     if DEBUG:
#         print("DEBUG:", todo_list)


# # Function to view only pending tasks
# def view_pending():
#     pending = [t for t in todo_list if t["status"] == "pending"]
#     if not pending:
#         print("No pending tasks.")
#         return

#     print("\nID   TASK NAME")
#     print("-" * 25)
#     for task in pending:
#         print(f"{task['id']:<4} {task['name']}")

#     if DEBUG:
#         print("DEBUG (all tasks):", todo_list)


# # Function to search tasks by keyword
# def search_task():
#     keyword = input("Enter keyword to search: ").strip().lower()
#     results = [t for t in todo_list if keyword in t["name"].lower()]

#     if not results:
#         print("No tasks found matching keyword.")
#         return

#     print("\nID   TASK NAME           STATUS")
#     print("-" * 35)
#     for task in results:
#         print(f"{task['id']:<4} {task['name']:<20} {task['status']}")

#     if DEBUG:
#         print("DEBUG (all tasks):", todo_list)


# # -----------------------------
# # Main program loop
# # -----------------------------
# while True:
#     print("\n---- MENU ----")
#     print("1. Add Task")
#     print("2. View All Tasks")
#     print("3. Update Task")
#     print("4. Delete Task")
#     print("5. View Pending Tasks")
#     print("6. Search Task")
#     print("7. Exit")

#     choice = input("Enter your choice (1-7): ").strip()

#     if choice not in ("1","2","3","4","5","6","7"):
#         print("Invalid choice. Enter 1-7.")
#         continue

#     if choice == "1":
#         add_task()
#     elif choice == "2":
#         view_tasks()
#     elif choice == "3":
#         update_task()
#     elif choice == "4":
#         delete_task()
#     elif choice == "5":
#         view_pending()
#     elif choice == "6":
#         search_task()
#     elif choice == "7":
#         print("Exiting program. Goodbye!")
#         break



# ==================================



# todo_list=[]#list of dict
# task_num=1
# print("\n     MENU     ")
# print("1.Add task")
# print("2.view tasks")
# print("3.Edit/Update task")
# print("4.view  pending tasks")
# print("5.delte task")
# print("6.Exit")
# while True:
#     user_choice=input("\nEnter your choice (1-6): ").strip()#user can enter num with space
#     if user_choice not in ("1","2","3","4","5","6"):
#         print(f"your choice: ({user_choice}) is not valid.choose only (1-6)")
#         continue
#     if user_choice=="6":
#         print("\nExiting...Goodbye!")
#         break
#     elif user_choice=="1":
#         print("\n-----ADD TASK-----")
#         user_task=input("enter Task: ")
#         if not user_task.strip():
#             print(f"You entered task:({user_task}) is not valid")
#             continue
#         # appending the dict into list since it is list of dict
#         tasks={"sno":task_num,"task":user_task,"status":"pending"}
#         todo_list.append(tasks)
#         task_num+=1
#         print("DEBUG: ",todo_list)
        
#     elif user_choice=="2":
#         print("\n----VIEW TASKS----")
#         if not todo_list:
#             print("no tasks avaible")
#             continue
#         print()
#         print(f"{"SNO":<5}{"TASK":<15}{"STATUS"}")
#         print("-"*29)
#         for item in (todo_list):
#             print(f"{item["sno"]:<5}{item["task"]:<18}{item["status"]}")

#     elif user_choice=="3":
#         print("\n----EDIT TASK----")
#         if not todo_list:
#             print("Task list is empty..add task to edit")
#             continue
        
       
        
#         print("\n----your tasks----")
#         for item in (todo_list):
#             print(f"\n{item["sno"]:<5}{item["task"]:<9}{item["status"]}")
#             print("-"*21)
#         tasknum_update=input("\nenter task number to Edit: ")
#         if not tasknum_update.isdigit():
#             print("invalid task number,please choose only digits")
#             continue
#         tasknum_update=int(tasknum_update)
#         for items in todo_list:
#             if items["sno"]==tasknum_update:
#                 if items["status"]=="Done":
#                     print(f"your task is done already..")
#                     break
#                 else:
                    
#                     items["status"]="Done"
#                     print(f"\nyour task {tasknum_update} is marked as Done")
#                     print("DEBUG",todo_list)
#                     break
            
#         else:
#             print(f"your task number: {tasknum_update} not Existed..")
            
      
        
#     elif user_choice=="4":
#         print("\n----VIEW PENDING TASKS----")
#         if not todo_list:
#             print("no tasks available, add some tasks first")
#             continue
#         pending_tasks=[f"{items["sno"]}:{items["task"]}"for items in todo_list if items["status"]=="pending"]
        
#         if pending_tasks:
#                 for task in pending_tasks:
#                     print(f"{task}")
#         else:
#             print("no pending tasks")
                
    
        
#     elif user_choice=="5":
#         print("\n----Delte Task----")
#         if not todo_list:
#             print("no tasks available task list is empty (choose 1 to add)")
#             continue
#         for items in todo_list:
#             print(f"{items["sno"]}:{items["task"]}---{items["status"]}")
#             print()
#         delete_task=input("enter task number to delete: ")
#         if  not delete_task.isdigit():
#             print("invalid task number,enter only digits to delte")
            
#         delete_task=int(delete_task)
#         new_list=[item for item in todo_list if item["sno"]!=delete_task]
#         if len(new_list)<len(todo_list):
#             todo_list=new_list
#             print(todo_list)

            
#         else:
#             print(f"task:{delete_task} not existed in the list")
        
                


#============================
