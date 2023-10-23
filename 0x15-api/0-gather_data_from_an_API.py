#!/usr/bin/python3
""""""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_json = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos_json = requests.get(
            url + "todos",
            params={"userId": sys.argv[1]}
            ).json()
    completed = [i.get("title") for i in
                 todos_json if i.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user_json.get("name"), len(completed), len(todos_json)))
    [print("\t {}".format(j)) for j in completed]
