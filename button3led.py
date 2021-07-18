"""
Press button light 3 lights one at a time

REQUIRED HARDWARE:
* Red LED on pin GP14
* Yellow Led on GP12
* Blue LED on GP11

* Button on GP13
"""
import board
import digitalio
import time

rled = digitalio.DigitalInOut(board.GP14)
rled.direction = digitalio.Direction.OUTPUT
yled = digitalio.DigitalInOut(board.GP12)
yled.direction = digitalio.Direction.OUTPUT
bled = digitalio.DigitalInOut(board.GP11)
bled.direction = digitalio.Direction.OUTPUT

button = digitalio.DigitalInOut(board.GP13)
button.switch_to_input(pull=digitalio.Pull.DOWN)

while True:
    if button.value:
        rled.value = True
        time.sleep(0.5)
        yled.value = True
        time.sleep(0.5)
        bled.value = True
        time.sleep(0.5)
        
    rled.value = False
    time.sleep(0.5)
    yled.value = False
    time.sleep(0.5)
    bled.value = False
    time.sleep(0.5)
