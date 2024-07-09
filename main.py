import time
from machine import I2C, Pin
from I2C_LCD import I2CLcd

class Initialize:
    def __init__(self, i2c_channel, sda_pin, scl_pin, freq=400000, address=None, rows=2, cols=16):
        self.i2c = I2C(i2c_channel, sda=Pin(sda_pin), scl=Pin(scl_pin), freq=freq)
        self.lcd_address = address or self.i2c.scan()[0]
        self.lcd = I2CLcd(self.i2c, self.lcd_address, rows, cols)

    def clear(self):
        self.lcd.clear()

    def move_to_position(self, row, col):
        self.lcd.move_to(row, col)

    def print(self, text, row, delay=0.2):
        padded_text = ' ' * 16 + text + ' ' * 16
        for i in range(len(padded_text) - 15):
            self.move_to_position(row, 0)
            self.lcd.putstr(padded_text[i:i + 16])
            print(padded_text[i:i + 16])
            time.sleep(delay)

def read_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        total_lines = len(lines)
        total_chars = sum(len(line.strip()) for line in lines)
    return lines, total_lines, total_chars

def read_csv_file(filename):
    with open(filename, 'r') as file:
        lines = [', '.join(line.strip().split(',')) for line in file.readlines()]
        total_lines = len(lines)
        total_chars = sum(len(line) for line in lines)
    return lines, total_lines, total_chars

def get_reader_function(filename):
    return read_csv_file if filename.endswith(".csv") else read_file

def print_file_content(filename, lcd, delay=0.2):
    read_func = get_reader_function(filename)
    try:
        lines, total_lines, total_chars = read_func(filename)
        print(f"Total lines: {total_lines}, Total characters: {total_chars}, File: {filename}")
        
        while True:
            based_message(lcd, "start")
            for line in lines:
                lcd.clear()
                lcd.print(line.strip(), 0, delay)
                time.sleep(1)
            based_message(lcd, "end")
    except OSError as os_error:
        print(f"OSError: {os_error}")
    except Exception as error:
        print(f"Exception: {error}")

def based_message(lcd, position):
    current_time = time.localtime()
    current_hour = current_time[3]
    if 5 <= current_hour < 12:
        message = "Good morning, have a nice day"
    elif 12 <= current_hour < 18:
        message = "Good afternoon, have a nice day"
    elif 18 <= current_hour < 22:
        message = "Good evening, have a nice day"
    else:
        message = "Good night, have a nice day"
    
    lcd.clear()
    lcd.print(message, 0)
    time.sleep(2)

def main():
    try:
        initialize = Initialize(i2c_channel=1, sda_pin=14, scl_pin=15)
        print_file_content("file.txt", initialize, delay=0.2)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

