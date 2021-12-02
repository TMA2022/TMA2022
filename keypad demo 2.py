# demo 1
# 4X4 Matrix Keypad Input Test

from machine import Pin
from time import sleep

# CONSTANTS
KEY_UP   = const(0)
KEY_DOWN = const(1)
#KEY_UP = 0
#KEY_DOWN = 1

keys = [['1', '2', '3', 'A'], ['4', '5', '6', 'B'], ['7', '8', '9', 'C'], ['*', '0', '#', 'D']]

# Pin names for Pico
rows = [23, 19, 18, 5]
cols = [15, 27, 26, 25]

# set pins for rows as outputs
myRowPins = [Pin(pin_name, mode=Pin.OUT) for pin_name in rows]

# set pins for cols as inputsstarting
myColPins = [Pin(pin_name, mode=Pin.IN, pull=Pin.PULL_DOWN) for pin_name in cols]

def initNow():
    for row in range(0,4):
        for col in range(0,4):
            myRowPins[row].value(0)
    
def scanNow(row, col):
    """ scan the keypad """

    # set the current column to high
    myRowPins[row].value(1)
    key = None
    # check for keypressed events
    if myColPins[col].value() == KEY_DOWN:
        key = KEY_DOWN
    if myColPins[col].value() == KEY_UP:
        key = KEY_UP
    myRowPins[row].value(0)

    # return the key state
    return key

print("starting")

# set all the columns to low
initNow()

while True:
    for row in range(4):
        for col in range(4):
            key = scanNow(row, col)
            if key == KEY_DOWN:
                print("Key Pressed", keys[row][col])
                last_key_press = keys[row][col]
