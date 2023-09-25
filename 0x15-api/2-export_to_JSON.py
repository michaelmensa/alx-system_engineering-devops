#!/usr/bin/python3
''' Accessing a REST API for todo list of employees '''

import json
import requests
import sys


if __name__ == '__main__':
    empID = sys.argv[1]
    baseUrl = 'https://jsonplaceholder.typicode.com/users'
    url = baseUrl + '/' + empID

    response = requests.get(url)
    username = response.json().get('username')

    todoUrl = url + '/todos'
    response = requests.get(todoUrl)
    tasks = response.json()
    my_dict = {empID: []}
    for task in tasks:
        value_dict = {
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
                }
        my_dict[empID].append(value_dict)
    json_file = f'{empID}.json'
    with open(json_file, 'w') as file_json:
        json.dump(my_dict, file_json)
