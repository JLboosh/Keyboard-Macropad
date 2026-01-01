import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros


keyboard = KMKKeyboard()

macros = Macros()

keyboard.modules.append(macros)

PINS = [board.D3, board.D0, board.D2, board.D4, board.A0, board.A3, board.A1, board.D7, board.A2]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)


keyboard.keymap = [
    [KC.A, 
     KC.Z, 
     KC.X, 
     KC.C,
     KC.SPACE,
     KC.LEFT,
     KC.DOWN,
     KC.RIGHT,
     KC.UP,]
]

if __name__ == '__main__':
    keyboard.go()
