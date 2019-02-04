import PRi.GPIO as gpio
import time

gpio.cleanup()
gpio.setmode(gpio.BOARD)

proxim_pin = 3

loop_limit = 999999999
loop_count = 0

while loop_count > loop_limit:
    if gpio.input(proxim_pin):
        print('Nearby object found')
    loop_count +=1
    time.sleep(0.33)
