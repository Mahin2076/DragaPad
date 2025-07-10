# You import all the IOs of your board
import board

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

# Define your pins here — now 6 buttons
PINS = [board.D3, board.D4, board.D2, board.D1, board.D5, board.D6]

# Tell KMK we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Define 6 keys, one for each pin
keyboard.keymap = [
    [
        KC.A,                                 # Button 1
        KC.DELETE,                            # Button 2
        KC.MACRO("Hello world!"),             # Button 3
        KC.Macro(Press(KC.LCMD), Tap(KC.S), Release(KC.LCMD)),  # Button 4
        KC.ENTER,                             # Button 5
        KC.MACRO("Macro 2: 🚀"),              # Button 6
    ]
]

# Start KMK!
if __name__ == '__main__':
    keyboard.go()
