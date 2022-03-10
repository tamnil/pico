# raspberry pico

CTRL-A - enter REPL mode
CTRL-B - enter normal REPL mode
CTRL-C - interrupt a running program
CTRL-D - soft reset
CTRL-E - paste mode

####################################33

rshell 'cp main.py /pyboard ; repl ~ import main ~'
rshell 'cp main.py /pyboard ; repl ~ machine.reset() ~'
rshell 'repl ~ machine.reset() ~'

echo a > /dev/ttyACM0



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


<(obj,ev)>  poll:

import sys,uselect
sp=uselect.poll()
sp.register(sys.stdin,uselect.POLLIN)
def read1():
    return(sys.stdin.read(1) if sp.poll(0) else None)


POLLERR : 8
POLLHUP  : 16
POLLIN : 1
POLLOUT : 4


<poll> poll.ipoll(timeout=-1, flags=0, /)


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


###########################################

Hardware Timers


Timer.init(*, mode=Timer.PERIODIC, period=- 1, callback=None)

Timer.deinit()


Timer.ONE_SHOT
Timer.PERIODIC


t = Timer()
t.init(<...>, callback = fn(<Timerobj))




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


## irq().flags()


 IRQs 0-3 are visible from to the processor, 4-7 are internal to the state machines.

 ### flags staates
irq/int/hex/bin
 0 - 256  - 0x100h  - 0001 0000 0000
 1 - 512  - 0x200h  - 0010 0000 0000
 2 - 1024 - 0x400h  - 0100 0000 0000
 3 - 2048 - 0x800h  - 1000 0000 0000


The emergency exception buffer¶
If an error occurs in an ISR, MicroPython is unable to produce an error report unless a special buffer is created for the purpose. Debugging is simplified if the following code is included in any program using interrupts.

import micropython
micropython.alloc_emergency_exception_buf(100)
The emergency exception buffer can only hold one exception stack trace. This means that if a second exception is thrown during the handling of an exception while the heap is locked, that second exception’s stack trace will replace the original one - even if the second exception is cleanly handled. This can lead to confusing exception messages if the buffer is later printed.


## USB reset

# all:

```

for i in /sys/bus/pci/drivers/[uoex]hci_hcd/*:*; do
  [ -e "$i" ] || continue
  echo "${i##*/}" > "${i%/*}/unbind"
  echo "${i##*/}" > "${i%/*}/bind"
done

```

### debug ISR Exception:

micropython.alloc_emergency_exception_buf(size)
Allocate size bytes of RAM for the emergency exception buffer (a good size is around 100 bytes). The buffer is used to create exceptions in cases when normal RAM allocation would fail (eg within an interrupt handler) and therefore give useful traceback information in these situations.

A good way to use this function is to put it at the start of your main script (eg boot.py or main.py) and then the emergency exception buffer will be active for all the code following it.
