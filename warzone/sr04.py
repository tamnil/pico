import machine
from machine import Timer
import time
from machine import Pin
import rp2

machine.freq(200000000)
pins = {"trigger": (0, Pin.OUT, Pin.PULL_DOWN), "echo": (1, Pin.IN, Pin.PULL_DOWN)}


class Sr04:
    def __init__(self, pins):
        self.x = time.ticks_us()
        self.p_tr = Pin(0, Pin.OUT)
        self.p_tr.off()

    a = "dsda"

    @rp2.asm_pio()
    def irq_test():
        wrap_target()
        wait(1, pin, 1)
        irq(0)
        wait(0, pin, 1)
        irq(1)
        wrap()

    @rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
    def irq_trigger():
        wrap_target()
        set(pins, 1)
        set(x, 1)
        label("pre")
        jmp(x_dec, "pre")[31]
        set(pins, 0)
        set(x, 20)
        label("post")
        jmp(x_dec, "post")[31]
        wrap()


sr04 = Sr04(pins)

z = {"time": {"init": 0, "end": 0, "delta": 0}}


def set_time(pio):
    flag = pio.irq().flags()
    if flag == 256:
        z["time"]["init"] = time.ticks_us()
    elif flag == 512:
        z["time"]["end"] = time.ticks_us()
        z["time"]["delta"] = time.ticks_diff(z["time"]["end"], z["time"]["init"])


rp2.PIO(0).irq(set_time)


sm = rp2.StateMachine(0, sr04.irq_test, freq=200000000)
sm_trigger = rp2.StateMachine(1, sr04.irq_trigger, freq=5000, set_base=Pin(0))
sm.active(1)

sm_trigger.active(1)
tm0 = machine.Timer()


while 1:
    time.sleep(0.01)
    print("x", z["time"])
