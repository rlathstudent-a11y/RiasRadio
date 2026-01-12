# You import all the IOs of your board
import board
import pwmio 
import time


# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Define your pins here!
PINS = [board.D7, board.D8, board.D9, board.D10]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Define a speaker on pin D6
speaker = pwmio.PWMOut(board.D6, duty_cycle=0, frequency=440, variable_frequency=True)
    
# Function to play a tone
def play_tone(frequency, duration=0.5):
    speaker.frequency = frequency
    speaker.duty_cycle = 32768  # 50% duty cycle
    time.sleep(duration)
    speaker.duty_cycle = 0  # Turn off the speaker

# Define macros for different tones

def tone1(keyboard):
    play_tone(330)  # E4

def tone2(keyboard):
    play_tone(392)  # G4

def tone3(keyboard):
    play_tone(440)  # A4

def tone4(keyboard):
    play_tone(523)  # C5

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [KC.MACRO(tone1), KC.MACRO(tone2), KC.MACRO(tone3), KC.MACRO(tone4),]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()