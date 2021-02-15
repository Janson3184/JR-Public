'''
Using ThreadPoolExecutor map from futures

from https://www.youtube.com/watch?v=5_K8GwZ_268
'''

from concurrent import futures
import requests
import datetime

nums = range(1,100)

url_tpl = 'http://jsonplaceholder.typicode.com/todos/{}'

def get_data(myid):
    '''
    Some example function to run multiple times
    '''

    url = url_tpl.format(myid)
    return requests.get(url).text


'''
This is the part that runs the function, gets
some data and returns them in order...
'''

with futures.ThreadPoolExecutor(12) as executor:
    results = executor.map(get_data, nums)

stop_multi = datetime.datetime.now()

# In the order of the original iterator...
for result in list(results):
    print(result)
