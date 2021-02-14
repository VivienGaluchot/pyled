#!/usr/bin/python3

import pigpio
import time
import colorsys

pi = pigpio.pi()
if not pi.connected:
    print("not connected to pigpiod")
    exit(1)

# HW configuration
MAX_COLOR=255

RED_PIN=17
GREED_PIN=22
BLUE_PIN=27


def set_color(red, green, blue):
    pi.set_PWM_dutycycle(RED_PIN, red)
    pi.set_PWM_dutycycle(GREED_PIN, green)
    pi.set_PWM_dutycycle(BLUE_PIN, blue)


while True:
    for i in range(0, 100):
        r, g, b = colorsys.hsv_to_rgb(i / 100, 1, 1)
        set_color(r * MAX_COLOR, g * MAX_COLOR, b * MAX_COLOR)
        time.sleep(.05)