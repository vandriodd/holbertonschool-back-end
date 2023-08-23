#!/usr/bin/python3
"""
2-export_to_JSON module:
Retrieve and store employee information and TODO list in JSON format
"""
import json
import requests
from sys import argv


if __name__ == "__main__":

    employee_id = argv[1]

    employee_info = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{id}').json()
    employee_todos_list = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{id}/todos').json()

    username = employee_info['username']
    filename = f"{id}.json"

    user_data = {id: []}
    for todo in employee_todos:
        user_data[employee_id].append({
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": username
        })

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(user_data, file, indent=4)
