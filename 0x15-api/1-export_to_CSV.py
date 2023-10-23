#!/usr/bin/python3
"""script to export data in the CSV format"""
import requests
import sys
import csv


def emp_data(id):
    url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    resp = requests.get(url)
    resp_json = resp.json()
    user_id = resp_json.get("id")
    username = resp_json.get("username")
    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
    todos = requests.get(url)
    todos_json = todos.json()
    csv_fname = "{}.csv".format(user_id)
    with open(csv_fname, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        csv_writer.writerow(["USER_ID", "USERNAME",
                             "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todos_json:
            completed = "True" if task.get("completed") else "False"
            task_title = task.get("title")
            csv_writer.writerow([user_id, username, completed, task_title])


if __name__ == "__main":
    emp_data(sys.argv[1])
