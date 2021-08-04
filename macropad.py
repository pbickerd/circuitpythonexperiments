# Wiring
# Test LED on GP14
# 100 ohm resister in front of led
# GND on 38 to -RAIL
# -RAIL to GND on LED
#
# Key wiring
# 3V3 to + on bottom row of breadboard - +RAIL
# Key 1 to GP0 and +RAIL
# Key 2 to GP1 and +RAIL
# Key 3 to GP2 and +RAIL
# Key 4 to GP3 and +RAIL
# Key 5 to GP12 and +RAIL


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

# Setup LED for testing keys
led = digitalio.DigitalInOut(board.GP14)
led.direction = digitalio.Direction.OUTPUT

# Setup key pins
key1 = digitalio.DigitalInOut(board.GP0)
key1.switch_to_input(pull=digitalio.Pull.DOWN)

key2 = digitalio.DigitalInOut(board.GP1)
key2.switch_to_input(pull=digitalio.Pull.DOWN)

key3 = digitalio.DigitalInOut(board.GP2)
key3.switch_to_input(pull=digitalio.Pull.DOWN)

key4 = digitalio.DigitalInOut(board.GP3)
key4.switch_to_input(pull=digitalio.Pull.DOWN)

key5 = digitalio.DigitalInOut(board.GP12)
key5.switch_to_input(pull=digitalio.Pull.DOWN)


# Main code - just loop listening for key presses
while True:
    if key1.value:
        print("key1 pressed")
        led.value = True
        kbd.send(Keycode.A)
        #layout.write(' test\n')
        time.sleep(0.5)
    if key2.value:
        print("key2 pressed")
        led.value = True
        kbd.send(Keycode.B)
        #layout.write(' test\n')
        time.sleep(0.5)
    if key3.value:
        print("key3 pressed")
        led.value = True
        kbd.send(Keycode.C)
        #layout.write(' test\n')
        time.sleep(0.5)
    if key4.value:
        print("key4 pressed")
        led.value = True
        kbd.send(Keycode.D)
        #layout.write(' test\n')
        time.sleep(0.5)
    if key5.value:
        print("key5 pressed")
        led.value = True
        kbd.send(Keycode.E)
        #layout.write(' test\n')
        time.sleep(0.5)

    led.value = False


