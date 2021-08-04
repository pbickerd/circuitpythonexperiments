"""
Wiring
  Screen:
    GND on screen to GND on pico
    VCC on screen to VBUS on pico
    SDA on screen to GP0 on pico
    SCL on screen to GP1 on pico
"""


import time
import board
import busio

i2c = busio.I2C(board.GP1, board.GP0)

while not i2c.try_lock():
    pass

try:
    while True:
        print("I2C addresses found:", [hex(device_address)
              for device_address in i2c.scan()])
        time.sleep(2)

finally:  # unlock the i2c bus when ctrl-c'ing out of the loop
    i2c.unlock()