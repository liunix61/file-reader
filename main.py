import time
from machine import I2C, Pin
from I2C_LCD import I2CLcd

class Initialize:
    def __init__(self, i2c_channel, sda_pin, scl_pin, freq=400000):
        self.i2c = I2C(i2c_channel, sda=Pin(sda_pin), scl=Pin(scl_pin), freq=freq)
        self.devices = self.i2c.scan()
        if self.devices:
            self.lcd = I2CLcd(self.i2c, self.devices[0], 2, 16)
        else:
            print("I2C not found.")

    def print(self):
        if self.lcd:
            self.lcd.move_to(0, 0)
            self.lcd.putstr("Hello, world!")

def main():
    try:
        initialize = Initialize(i2c_channel=1, sda_pin=14, scl_pin=15)
        if initialize.lcd:
            initialize.print()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()