#!/usr/bin/python3
"""f,f,f,"""
import requests
import sys


def emp_data(id):
    # Make a GET request to retrieve user information
    user_url = f"https://jsonplaceholder.typicode.com/users/{id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data["name"]

    # Make a GET request to retrieve the user's TODO list
    todos_url = f"https://jsonplaceholder.typicode.com/users/{id}/todos"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculate the number of completed and total tasks
    completed_tasks = [task for task in todos_data if task["completed"]]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todos_data)

    # Display the results
    print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)
    emp_data(sys.argv[1])
