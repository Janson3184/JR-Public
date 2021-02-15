
from concurrent import futures
import requests


nums = range(1,11)

url_tpl = 'http://jsonplaceholder.typicode.com/todos/{}'

def get_data(myid):
    '''
    Some example function to run multiple times
    '''

    url = url_tpl.format(myid)
    return requests.get(url).text


'''
Only exits the entire block when all 
pending futures are completed
'''
with futures.ThreadPoolExecutor(12) as executor:
    jobs = [executor.submit(get_data, num) for num in nums]
    '''These jobs (futures) are submitted to 
    the as_completed function and iterated through as 
    they complete.
    '''
    for comp_job in futures.as_completed(jobs):
        print(comp_job.result())
