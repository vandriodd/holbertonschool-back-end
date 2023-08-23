#!/usr/bin/python3
"""
0-gather_data_from_an_API module:
Fetches and displays the progress of an employee's TODO list
"""

import requests
from sys import argv

if __name__ == "__main__":
    employee_id = argv[1]
    completed_task = 0
    total_tasks = 0
    completed_task_titles = []

    employee_info = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    employee_todo_list = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')

    for todo in employee_todo_list.json():
        if todo.get('completed') is True:
            completed_task += 1
            total_tasks += 1
            completed_task_titles.append(todo.get('title'))
        else:
            total_tasks += 1

    name = employee_info.json().get('name')

    print(
        f"Employee {name} is done with tasks({completed_task}/{total_tasks}):")
    for task in completed_task_titles:
        print(f"\t {task}")
