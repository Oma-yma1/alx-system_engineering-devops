#!/usr/bin/python3
"""   export data in the CSV format"""
import csv
import requests
import sys

if __name__ == "__main__":
    user_json = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user_js = requests.get(url + "users/{}".format(user_json)).json()
    username = user_js.get("username")
    todos_json = requests.get(
            url + "todos",
            params={"userId": user_json}
            ).json()
    with open("{}.csv".format(user_json), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_json, username, i.get("completed"), i.get("title")]
         ) for i in todos_json]
