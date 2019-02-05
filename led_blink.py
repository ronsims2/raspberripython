import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BOARD)

led_pin = 13

gpio.setup(led_pin, gpio.OUT)

while True:
    gpio.output(led_pin, True)
    time.sleep(1)
    gpio.output(led_pin, False)
    time.sleep(1)