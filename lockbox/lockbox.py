#!/usr/bin/env python3

from time import sleep
import RPi.GPIO as gpio

class Lockbox:
    def __init__(self, pin=3):
        self.unlock_pin = pin
        self.setup(pin)

    def setup(self, pin=3):
        self.unlock_pin = pin
        gpio.setmode(gpio.BOARD)
        gpio.setup(self.unlock_pin, gpio.OUT)

    def unlock_box(self):
            self.toggle_lock(False)

    def lock_box(self):
            self.toggle_lock(True)

    def toggle_lock(self, unlock):
        gpio.output(self.unlock_pin, unlock)
        sleep(1)


    def cycle_lock(self, cycle_count=3, duration=3):
        cycles = cycle_count
        if cycles == 0 or cycles % 2 == 0:
            cycles += 1

        for i in range(cycles):
            self.toggle_lock((i + 1) % 2 != 0)
            sleep(duration)
