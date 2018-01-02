from time import sleep
from rrpi import gpio


gpio.set_bcm_mode()

light = gpio.PinOut(17)

val = True
while True:
    light.set(val)
    val = not val
    sleep(1.0)
