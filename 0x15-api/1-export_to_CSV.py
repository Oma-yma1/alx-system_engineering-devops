#!/usr/bin/python3
"""script to export data in the CSV format"""
import requests
import sys


def emp_data(id):
    url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    resp = requests.get(url)
    resp_json = resp.json()
    name = resp_json["name"]
    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
    todos = requests.get(url)
    todos_json = todos.json()
    num_task = len(todos_json)
    compleeted = 0
    task_list = ""
    name_file = "{}.csv".format(id)
    with open(name_file, "a") as fd:
        for task in todos_json:
            completed = task.get("completed")
            titlee = task.get("titlee")
            csv = "\"{}\",\"{}\",\"{}\",\"{}\"\n".format(id, name,
                                                         completed, titlee)
            fd.write(csv)


if __name__ == "__main__":
    emp_data(sys.argv[1])
