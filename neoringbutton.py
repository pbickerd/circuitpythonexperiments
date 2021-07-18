# HW Setup
# 3V to power rail
# Power rail to button
# GP15 to other side of button
# Neopixel control to GP0
# Neopixel ground to ground
# Neopixel VCC to VBUS

import time
import board
import digitalio
import board
import neopixel

# vars
speed = 0.5

# Setup neopixel
num_pixels = 16

pixels = neopixel.NeoPixel(board.GP0, num_pixels)
pixels.brightness = 0.5

# Setup buttons
button1 = digitalio.DigitalInOut(board.GP15)
button1.switch_to_input(pull=digitalio.Pull.DOWN)

while True:
    if button1.value:
        print("button1 pressed")
        pixels.fill((255,0,0))
        time.sleep(speed)
        pixels.fill((0,255,0))
        time.sleep(speed)
        pixels.fill((0,0,255))
        time.sleep(speed)
    pixels.fill((0, 0, 0))


