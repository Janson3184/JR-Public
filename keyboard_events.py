import datetime
import time

import keyboard

'''
From: https://pypi.org/project/keyboard/
'''

MAX_RECORDS = 81

start = datetime.datetime.now()

string = 'CH000the CH0quick CH0brown CH000fox CH0jumps CH00over CH000the CH00lazy CH000dog'

list = string.split(' ')    #   ['CH000the', 'CH0quick'... ]


def countdown(t):
    '''
    Countdown timer in seconds.  Not accurate.

    :argument t int
    '''

    print(f'Waiting {t} seconds.  Cursors ready...')
    for i in reversed(range(1,t+1)):
        print(i)
        time.sleep(1)


def scan_box():
    '''
    Sends commands to the keyboard.
    '''

    countdown(3)

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