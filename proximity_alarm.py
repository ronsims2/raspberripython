import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)

proxim_pin = 11
led_pin = 13

gpio.setup(proxim_pin, gpio.IN, gpio.PUD_DOWN)
gpio.setup(led_pin, gpio.OUT)

loop_limit = 999999999
loop_count = 0

while loop_count < loop_limit:
    gpio.output(led_pin, False)
    if gpio.input(proxim_pin):
        print('Nearby object found')
        gpio.output(led_pin, True)
    loop_count +=1
    time.sleep(0.33)

gpio.cleanup()
