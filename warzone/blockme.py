import time
import sys
import select
print('inti main')


micropython.kbd_intr(-1)

def run():
    count = 1
    while True:
        print('here',count)
        count +=1
        time.sleep(1)



run()
