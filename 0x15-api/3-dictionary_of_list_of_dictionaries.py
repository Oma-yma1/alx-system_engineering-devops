#!/usr/bin/python3
"""script to export data in the JSON format"""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users").json()
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            i.get("id"): [{
                "task": k.get("title"),
                "completed": k.get("completed"),
                "username": i.get("username")
            } for k in requests.get(url + "todos",
                                    params={"userId": i.get("id")}).json()]
            for i in user}, jsonfile)
