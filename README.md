# raspberry pico

CTRL-A - enter REPL mode
CTRL-B - enter normal REPL mode
CTRL-C - interrupt a running program
CTRL-D - soft reset
CTRL-E - paste mode

####################################33



micropython.kbd_intr(chr)

micropython.kbd_intr(-1)

micropython.kbd_intr(3)

https://docs.micropython.org/en/latest/library/micropython.html

####################################

import micropython
import select
import sys
micropython.kbd_intr(-1)
while True:
  while sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
    ch = sys.stdin.read(1)
    print("Got " + hex(ord(ch)))

################### clock #################

default system clock frequency of 125MHz, the minimum value of freq is 1908

machine.freq([hz])

################## State Machine ######################


 rp2.StateMachine(0, blink_1hz, freq=4000, set_base=Pin(0))



#################### Pin irq #######################

Pin.irq(handler=None, trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, *, priority=1, wake=None, hard=False)

trigger configures the event which can generate an interrupt. Possible values are:

Pin.IRQ_FALLING interrupt on falling edge.

Pin.IRQ_RISING interrupt on rising edge.

Pin.IRQ_LOW_LEVEL interrupt on low level.

Pin.IRQ_HIGH_LEVEL interrupt on high level.




pin19 = Pin(19, Pin.IN, Pin.PULL_UP)
def hello(a):
    print('hello',a)

pin19.irq(handler=hello,trigger=Pin.IRQ_FALLING)

##############################################3


    # source constants for wait
    "gpio": 0,
    # "pin": see below, translated to 1
    # "irq": see below function, translated to 2
    # source/dest constants for in_, out, mov, set
    "pins": 0,
    "x": 1,
    "y": 2,
    "null": 3,
    "pindirs": 4,
    "pc": 5,
    "status": 5,
    "isr": 6,
    "osr": 7,
    "exec": 8,  # translated to 4 for mov, 7 for out
    # operation functions for mov's src
    "invert": lambda x: x | 0x08,
    "reverse": lambda x: x | 0x10,
    # jmp condition constants
    "not_x": 1,
    "x_dec": 2,
    "not_y": 3,
    "y_dec": 4,
    "x_not_y": 5,
    "pin": 6,
    "not_osre": 7,
    # constants for push, pull
    "noblock": 0x01,
    "block": 0x21,
    "iffull": 0x40,
    "ifempty": 0x40,
    # constants and modifiers for irq
    # "noblock": see above
    # "block": see above
    "clear": 0x40,
    "rel": lambda x: x | 0x10,
    # functions
    "wrap_target": None,
    "wrap": None,
    "label": None,
    "word": None,
    "nop": None,
    "jmp": None,
    "wait": None,
    "in_": None,
    "out": None,
    "push": None,
    "pull": None,
    "mov": None,
    "irq": None,
    "set": None,
