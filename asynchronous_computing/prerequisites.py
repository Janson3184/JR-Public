'''
This describes a parallel job before converging into a terminal function
which completes.  The parallel jobs upstream are considered "prerequisites".

An example is that you must "take out the trash, do recycling, do homework" before you can
go outside and play.

In this example it'll go in the order of:

info + tweets >  process details > cleanup

'''


from concurrent import futures

def get_info():
    pass

def get_tweets():
    pass

def process_details():
    pass


with futures.ThreadPoolExecutor(2) as e:    # Only two workers this time...
    info_job = e.submit(get_info)
    tweets_job = e.submit(get_tweets)
    futures.wait([info_job, tweets_job], futures.ALL_COMPLETED) #   Only move beyond when both jobs complete.
    info = info_job.result()
    tweets = tweets_job.result()

    #   Feed completed results as arguments into process_details function
    process_job = e.submit(process_details, info, tweets)
    futures.wait([process_job], futures.ALL_COMPLETED)



