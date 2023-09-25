#!/usr/bin/python3
''' Accessing a REST API for todo list of employees '''

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
    csv_file = f'{empID}.csv'
    with open(csv_file, 'w') as file:
        for task in tasks:
            for_mat = '"{}","{}","{}","{}"\n'.format(
                    empID, username, task.get('completed'), task.get('title'))
            file.write(for_mat)
