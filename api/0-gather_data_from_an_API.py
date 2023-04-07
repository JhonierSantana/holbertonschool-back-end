#!/usr/bin/python3
'''returns information about his/her TODO list progress.'''
import pandas as pd
import requests
import sys
'''data analysis'''
if __name__ == '__main__':
    reponse = requests.get('https://jsonplaceholder.typicode.com/todos/')
    '''data analysis'''
    data = pd.read_json(reponse.text)
    total_number_of_task = len(data[data['userId'] == int(sys.argv[1])])
    completed = len(data[(data['userId'] == int(
        sys.argv[1])) & (data['completed'] == True)])

    reponse2 = requests.get('https://jsonplaceholder.typicode.com/users/')
    data2 = pd.read_json(reponse2.text)
    employee_name = data2[data2['id'] == int(sys.argv[1])]['name'].values[0]
    task_title = list(data[(data['userId'] == int(sys.argv[1])) & (
        data['completed'] == True)]['title'])

    print("Employee {} is done with tasks({}/{}):".format(employee_name,
          completed, total_number_of_task))

    for i in task_title:
        print("\t {}".format(i))
