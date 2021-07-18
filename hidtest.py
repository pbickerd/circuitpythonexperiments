import time

import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode


# Set up a keyboard device.
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

# Setup LEDs
bled = digitalio.DigitalInOut(board.GP0)
bled.direction = digitalio.Direction.OUTPUT
rled = digitalio.DigitalInOut(board.GP1)
rled.direction = digitalio.Direction.OUTPUT
yled = digitalio.DigitalInOut(board.GP2)
yled.direction = digitalio.Direction.OUTPUT

# Setup buttons
button1 = digitalio.DigitalInOut(board.GP13)
button1.switch_to_input(pull=digitalio.Pull.DOWN)

button2 = digitalio.DigitalInOut(board.GP12)
button2.switch_to_input(pull=digitalio.Pull.DOWN)

button3 = digitalio.DigitalInOut(board.GP11)
button3.switch_to_input(pull=digitalio.Pull.DOWN)

while True:
    if button1.value:
        print("button1 pressed")
        bled.value = True
        kbd.send(Keycode.A)
        layout.write(' penis\n')
        time.sleep(0.5)
    if button2.value:
        print("button2 pressed")
        rled.value = True
        kbd.send(Keycode.A)
        layout.write(' willy\n')
        time.sleep(0.5)
    if button3.value:
        print("button3 pressed")
        yled.value = True
        kbd.send(Keycode.A)
        layout.write(' wee wee\n')
        time.sleep(0.5)
    bled.value = False
    rled.value = False
    yled.value = False


