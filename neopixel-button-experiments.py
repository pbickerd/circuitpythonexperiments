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
speed = 0.2
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)

color_list = [RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, RED, YELLOW, GREEN, CYAN]

# Setup neopixel
num_pixels = 16

pixels = neopixel.NeoPixel(board.GP0, num_pixels)
pixels.brightness = 0.5

# Setup buttons
button1 = digitalio.DigitalInOut(board.GP15)
button1.switch_to_input(pull=digitalio.Pull.DOWN)

# Functions
def wheel(led,color):
        pixels[led] = color
        time.sleep(speed)

while True:
    if button1.value:
        print("button1 pressed")
        for i in range(num_pixels):
          wheel(i,color_list[i])

    pixels.fill((0, 0, 0))
