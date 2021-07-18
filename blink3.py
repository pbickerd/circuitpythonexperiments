"""
LED example for Pico. Blinks external LED on and off.

REQUIRED HARDWARE:
* LED on pin GP14.
"""
import time
import board
import digitalio

bled = digitalio.DigitalInOut(board.GP14)
bled.direction = digitalio.Direction.OUTPUT

yled = digitalio.DigitalInOut(board.GP13)
yled.direction = digitalio.Direction.OUTPUT

rled = digitalio.DigitalInOut(board.GP12)
rled.direction = digitalio.Direction.OUTPUT


while True:
    bled.value = True
    time.sleep(0.5)
    bled.value = False
    time.sleep(0.5)
    yled.value = True
    time.sleep(0.5)
    yled.value = False
    time.sleep(0.5)
    rled.value = True
    time.sleep(0.5)
    rled.value = False
    time.sleep(0.5)
    print("looped")