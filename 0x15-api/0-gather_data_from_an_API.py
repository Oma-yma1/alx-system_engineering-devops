#!/usr/bin/python3
"""returns information about TODO list progress for a given emp id"""
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
    compleated = 0
    list = ""
    for task in todos_json:
        if task.get("completed") is True:
            compleated += 1
            list += "\t " + task.get("title") + "\n"

    print("Employee {} is done with tasks({}/{}):".format(name,
                                                          compleated,
                                                          num_task))
    print(list[:-1])


if __name__ == "__main__":
    emp_data(sys.argv[1])
