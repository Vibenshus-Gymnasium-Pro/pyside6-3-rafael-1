import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QObject


loader = QUiLoader()


class Tictactoe(QObject):
    def __init__(self):
        super().__init__()
        self.ui = loader.load("window.ui", None)
        self.cross = True
        self.pressed_buttons = []

        # Creating a list of all the buttons, for use in the for loop connecting them all to the same slot with different parameters.
        self.buttons = [self.ui.button00, self.ui.button01, self.ui.button02, self.ui.button10, self.ui.button11, self.ui.button12, self.ui.button20, self.ui.button21, self.ui.button22]
        for button in self.buttons:
            button.clicked.connect( lambda checked, button=button : self.pressed(button))

    def pressed(self, button):
        # Check if the game is completed, and resets if so
        if len(self.pressed_buttons) >= 9:
            self.clear()
            return # Without this the game would clear and the first turn would happen during the same click.
        if button not in self.pressed_buttons:
            if self.cross == True:
                button.setText("X")
            else:
                button.setText("O")
            self.cross = not self.cross
            self.pressed_buttons.append(button)

    def clear(self):
        # Remove button text
        for button in self.buttons:
            button.setText("")
        # Remove buttons from pressed list
        self.pressed_buttons = []


program = QApplication.instance()
if program == None:
    program = QApplication(sys.argv)
tictactoe = Tictactoe()
tictactoe.ui.show()
program.exec()
