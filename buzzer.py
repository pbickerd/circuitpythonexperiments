# HW Setup
# 3V to power rail
# Power rail to button
# GP15 to other side of button

import time
import board
import digitalio
import pwmio

# Setup buttons
button1 = digitalio.DigitalInOut(board.GP15)
button1.switch_to_input(pull=digitalio.Pull.DOWN)

#Setup buzzer
buzzer = pwmio.PWMOut(board.GP14, frequency=660, duty_cycle=0, variable_frequency=True)


while True:
    if button1.value:
        print("button1 pressed")
        buzzer.duty_cycle = 2 ** 15
    buzzer.duty_cycle = 0 