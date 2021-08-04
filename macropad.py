# Wiring
# Test LED on GP14
# 100 ohm resister in front of led
# GND on 38 to -RAIL
# -RAIL to GND on LED
#
# Key wiring
# 3V3 to +

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


# Setup buttons
key1 = digitalio.DigitalInOut(board.GP0)
key1.switch_to_input(pull=digitalio.Pull.DOWN)



while True:
    if key1.value:
        print("key1 pressed")
        led.value = True
        #kbd.send(Keycode.A)
        #layout.write(' penis\n')
        time.sleep(0.5)
    led.value = False


