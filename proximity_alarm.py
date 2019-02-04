import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)

proxim_pin = 3

gpio.setup(proxim_pin, gpio.IN, gpio.PUD_DOWN)

loop_limit = 999999999
loop_count = 0

while loop_count < loop_limit:
    if gpio.input(proxim_pin):
        print('Nearby object found')
    loop_count +=1
    time.sleep(0.33)

gpio.cleanup()
