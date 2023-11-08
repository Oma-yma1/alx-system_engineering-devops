#!/usr/bin/python3
""" export data in the JSON format"""
import json
import requests
import sys

if __name__ == "__main__":
    id_user = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user_js = requests.get(url + "users/{}".format(id_user)).json()
    username = user_js.get("username")
    todos_js = requests.get(
            url + "todos",
            params={"userId": id_user}
            ).json()
    with open("{}.json".format(id_user), "w") as jsonfile:
        json.dump({id_user: [{
                "task": i.get("title"),
                "completed": i.get("completed"),
                "username": username
            } for i in todos_js]}, jsonfile)
