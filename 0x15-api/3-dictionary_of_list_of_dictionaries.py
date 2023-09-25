#!/usr/bin/python3
''' Accessing a REST API for todo list of employees '''

import json
import requests
import sys


if __name__ == '__main__':
    baseUrl = 'https://jsonplaceholder.typicode.com/users'

    response = requests.get(baseUrl)
    users = response.json()
    my_dict = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
        url = url + '/todos/'
        response = requests.get(url)
        tasks = response.json()
        my_dict = {user_id: []}
        for task in tasks:
            value_dict = {
                    "task": task.get('title'),
                    "completed": task.get('completed'),
                    "username": username
                    }
            my_dict[user_id].append(value_dict)
    json_file = f'todo_all_employees.json'
    with open(json_file, 'w') as file_json:
        json.dump(my_dict, file_json)
