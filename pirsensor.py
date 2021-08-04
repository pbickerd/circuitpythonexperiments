"""
REQUIRED HARDWARE:
* PIR sensor on pin GP28.
"""

import time
import board
import digitalio
import pwmio

#setup pir
pir = digitalio.DigitalInOut(board.GP28)
pir.direction = digitalio.Direction.INPUT


while True:
    print(pir.value)
    time.sleep(1)