import machine
from machine import Pin
import time
import select
import sys


count = 0
pin_trigger = machine.Pin(0,Pin.IN,Pin.PULL_UP)
pin_led = machine.Pin(25,Pin.OUT)
pin_led.off()

def action(pin):
    sys.stdout.write('y')

pin_trigger.irq(handler=action,trigger=Pin.IRQ_FALLING)


spoll = select.poll()
spoll.register(sys.stdin,select.POLLIN)
def readin():
    return (sys.stdin.read(1) if spoll.poll(0) else None)

while True:
    x = readin()
    if x == 'x':
        print('hell')
