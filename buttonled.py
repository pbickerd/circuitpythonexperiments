"""
Button and LED example for Pico. Turns on LED when button is pressed.

REQUIRED HARDWARE:
* Button switch on pin GP13.
* LED on pin GP14.
"""
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.GP14)
led.direction = digitalio.Direction.OUTPUT

button = digitalio.DigitalInOut(board.GP13)
button.switch_to_input(pull=digitalio.Pull.DOWN)

while True:
    if button.value:
        led.value = True
        time.sleep(0.5)
        led.value = False
        time.sleep(0.5)
        led.value = True
    led.value = False
