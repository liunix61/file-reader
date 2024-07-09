# Overview

On a classic whiteboard setup, using a MCU and an array of connected wires, the contents of a file are scrolled across the screen from right to left.

### I2C Communication

I2C (Inter-Integrated Circuit) is a two-wire serial communication mode used to connect microcontrollers and peripheral devices. It utilizes a serial data (SDA) line and serial clock (SCL) line (referred to as the I2C bus). Each device on the bus has a unique address and can function as a transmitter or receiver, enabling communication with other connected devices.

### LCD1602 

The LCD1602 display screen can show 2 lines of characters with 16 columns each. It supports displaying numbers, letters, symbols, and ASCII codes.

### Class I2CLcd

Before using the I2CLcd object, ensure that I2C_LCD.py and LCD_API.py are uploaded to the root directory of Raspberry Pi Pico. Then, add from I2C_LCD import I2CLcd to the top of your Python file.

Methods
* clear(): Clears the LCD1602 screen display.
* show_cursor(): Shows the cursor of the LCD1602.
* hide_cursor(): Hides the cursor of the LCD1602.
* blink_cursor_on(): Turns on cursor blinking.
* blink_cursor_off(): Turns off cursor blinking.
* display_on(): Turns on the display function of the LCD1602.
* display_off(): Turns off the display function of the LCD1602.
* backlight_on(): Turns on the backlight of the LCD1602.
* backlight_off(): Turns off the backlight of the LCD1602.
* move_to(cursor_x, cursor_y): Moves the cursor to a specified position.
* cursor_x: Column position.
* cursor_y: Row position.
* putchar(char): Prints the character on the LCD1602.
* putstr(string): Prints the string on the LCD1602.
