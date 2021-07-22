
pin19 = Pin(19, Pin.IN, Pin.PULL_UP)
def hello(a):
    print('hello',a)

pin19.irq(handler=hello,trigger=Pin.IRQ_FALLING)
