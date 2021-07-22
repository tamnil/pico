import time
import sys
import select
print('inti main')
def run():
    count = 1
    while True:
        #print()

        while sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            ch = sys.stdin.read(1)
            print(ch)
            count +=1
            #if (ch == 'as'):
                # 100 characters
            print( 'count:' + str(count) + ch )

run()
