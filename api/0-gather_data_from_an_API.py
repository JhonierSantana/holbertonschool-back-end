#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(api_url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(
        api_url + "todos", params={"userId": sys.argv[1]}).json()

    completed = []
    for task in todos:
        if task.get("completed") is True:
            completed.append(task.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    for complete in completed:
        print("\t {}".format(complete))
