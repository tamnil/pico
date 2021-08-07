from machine import Timer



cb = lambda x : print(x,'xval-cb1')
cb2 = lambda x : print(x,'xval - cb2')
# cb_counter = lambda x : print(x,'xval',counter,'counter val')

counter = 0

def cb_counter(timer):
    global counter
    counter +=1
    print(timer,counter,'cbcounter value')

a = Timer()
b  = Timer()
c  = Timer()

a.init(mode=Timer.PERIODIC, callback=cb,period=2000)
b.init(mode=Timer.ONE_SHOT,callback=cb2,period=4000)
c.init(mode=Timer.PERIODIC, callback=cb_counter,period=3000)
