#!/usr/bin/python3
"""returns information about for a given employee ID"""
import requests
import sys


def emp_data(id):
    url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    resp = requests.get(url)
    resp_json = resp.json()
    name = resp_json.get("name")
    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
    todos = requests.get(url)
    todos_json = todos.json()
    num_task = len(todos_json)
    compleeted = 0
    list = ""
    for task in todos_json:
        if task.get("completed") is True:
            compleeted += 1
            list += "\t " + task.get("title") + "\n"
    print("Employee {} is done with tasks({}/{}):".format(name,
                                                          compleeted,
                                                          num_task))
    print(list[:-1])


if __name__ == "__main__":
    emp_data(sys.argv[1])
