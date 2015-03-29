from pywinusb import hid
import time
import random

from SMTKeyboard import SMTKeyboard
from constants import constants

def random_color():
    return random.choice(constants.colors.keys())

def random_intensity():
    return random.choice(constants.levels.keys())

def shuffer(kbd):
    kbd.set_color('left',random_color(),random_intensity())
    kbd.set_color('middle',random_color(),random_intensity())
    kbd.set_color('right',random_color(),random_intensity())

if __name__ == "__main__":
    filter = hid.HidDeviceFilter(vendor_id = 6000, product_id = 65280)
    hid_device = filter.get_devices()
    device = hid_device[0]
    try:
        device.open(output_only = True )
        kbd = SMTKeyboard(device)
        for i in range(10):
            shuffer(kbd)
            time.sleep(0.1)
        kbd.set_mode("normal")
        print kbd.current
    finally:
        device.close()
