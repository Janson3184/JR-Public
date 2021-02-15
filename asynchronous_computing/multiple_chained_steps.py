'''
Imagine three lines each with multiple functions that never converge

Like going through a series of websites, and performing some action to each.

or looping through images and adding memes to each.
'''

from concurrent import futures

def get_img(myid):
    '''
    Just a placeholder function that takes a random amount of time.
    :param myid:
    :return:
    '''
    sleep(randint(1,5)/10)
    img = "{}.png".format(myid)
    print("\nGot image {}".format(img))
    return img

def add_meme_to_img(img_path):
    '''
    Again, just a placeholder function.
    :param img_path:
    :return:
    '''
    sleep(randint(1,5)/30)
    msg = "Added meme to image {}".format(img_path)
    print("\n" + msg)


with futures.ThreadPoolExecutor(12) as executor:
    jobs = [executor.submit(get_img, num) for num in nums]
    for comp_job in futures.as_completed(jobs):
        img_path = comp_job.result()
        executor.submit(add_meme_to_img, img_path)



