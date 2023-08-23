#!/usr/bin/python3
"""
1-export_to_CSV module:
Fetch employee information and their TODO list,
then writes this data to a CSV file
"""

import requests
from sys import argv

if __name__ == "__main__":

    id = argv[1]

    employee_info = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{id}')
    employee_todo_list = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{id}/todos')

    name = employee_info.json().get('username')
    filename = f"{id}.csv"
    with open(filename, "w", encoding="utf-8") as file:
        for todo in employee_todo_list.json():
            completed_status = todo.get('completed')
            task_title = todo.get('title')
            file.write(
                f'"{id}","{name}","{completed_status}","{task_title}"\n')
