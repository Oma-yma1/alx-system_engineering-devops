#!/usr/bin/python3
"""Returns information about TODO list progress FOR A GIVEN EMP ID"""
import requests
import sys


BASE_URL = "https://jsonplaceholder.typicode.com"


def get_data(id):
    try:
        response = requests.get(f"{BASE_URL}/users/{id}")
        data = response.json()
        name = data.get("name")
        todos_resp = requests.get(f"{BASE_URL}/todos?userId={id}")
        todos = todos_resp.json()
        completed_task = [task for task in todos if task["completed"]]
        num_complet = len(completed_task)
        total_task = len(todos)
        return name, num_complet, total_task, completed_task
    except requests.exceptions.RequestException as e:
        print("Error fetching data from the API:", e)
        sys.exit(1)


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <id>")
        sys.exit(1)
    id = int(sys.argv[1])
    name, num_complet, total_task, completed_task = get_data(id)
    print(f"Employee {name} is done with tasks({num_complet}/{total_task}):")

    for task in completed_task:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    main()
