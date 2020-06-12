import keyboard
import datetime
import time

'''
From: https://pypi.org/project/keyboard/
'''
MAX_RECORDS = 81

start = datetime.datetime.now()

string = 'CH000the CH0quick CH0brown CH000fox CH0jumps CH00over CH000the CH00lazy CH000dog'

list = string.split(' ')


def countdown(t):
    '''
    Countdown timer in seconds.  Not accurate.

    :argument t int
    '''
    print(f'Waiting {t-1} seconds.  Cursors ready...')
    for i in reversed(range(1,t)):
        print(i)
        time.sleep(1)


def scan_box():
    '''
    Sends commands to the keyboard.
    '''

    countdown(4)

    counter = 0
    while counter < MAX_RECORDS:
        for word in list:
            keyboard.write(word)
            keyboard.press_and_release('return')
            counter += 1


scan_box()

stop = datetime.datetime.now()

print(f'Elapsed: {stop-start}\nTime Per Scan: {(stop-start)/MAX_RECORDS}')

'''

'''