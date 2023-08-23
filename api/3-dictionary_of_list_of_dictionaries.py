#!/usr/bin/python3
"""
3-dictionary_of_list_of_dictionaries:
Consolidate and store user TODO list data in JSON format
"""
import json
import requests


if __name__ == "__main__":

    employee_info = requests.get(
        f'https://jsonplaceholder.typicode.com/users').json()
    todo_data = requests.get(
        f'https://jsonplaceholder.typicode.com/todos').json()

    consolidated_data = {}
    filename = "todo_all_employees.json"

    for user in employee_info:
        user_id = user.get('id')
        consolidated_data[user_id] = []
        for todo in todo_data:
            if user_id == todo.get('userId'):
                consolidated_data[user_id].append({
                    "username": user.get("username"),
                    "task": todo.get("title"),
                    "completed": todo.get("completed")
                })

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(consolidated_data, file)
