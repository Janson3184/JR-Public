from concurrent import futures

with futures.ThreadPoolExecutor(4) as e:    #   Only four workers...
    jobs = [e.submit(get_data, n) for n in nums]
    done, not_done = futures.wait(jobs, return_when=futures.FIRST_COMPLETED) # Or all completed or first exception...
    done_job = done.pop()
    print(done_job.result())

    for not_done_job in not_done:
        not_done_job.cancel()

    '''
    The program still has to cancel out of all running jobs...so not 
    technically terminating after first completed.
    '''
    print("Program finished - No running jobs.")

