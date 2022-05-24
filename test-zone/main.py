import machine


machine.freq()          # get the current frequency of the CPU
machine.freq(240000000) # set the CPU frequency to 240 MHz


class Hello():
    def __init__(self):
        print('hello init')
        self.x = 'asdf'


