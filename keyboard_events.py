import keyboard
import datetime
import time

'''
From: https://pypi.org/project/keyboard/
'''

start = datetime.datetime.now()

string = 'CH000the CH0quick CH0brown CH000fox CH0jumps CH00over CH000the CH00lazy CH000dog'

list = string.split(' ')
counter = 0

def scan_box(counter):
    print('Waiting 2 seconds.  Cursors ready...')
    time.sleep(2)
    while counter < 81:
        for word in list:
            keyboard.write(word)
            keyboard.press_and_release('return')
            counter += 1

scan_box(counter)

stop = datetime.datetime.now()

print(f'Elapsed: {stop-start}')

'''


'''