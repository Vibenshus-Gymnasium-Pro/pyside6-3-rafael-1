import sys
import logic

from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QObject


loader = QUiLoader()


class Tictactoe(QObject):
    def __init__(self):
        super().__init__()
        self.ui = loader.load("window.ui", None)
        self.cross = True
        self.game_over = False
        self.pressed_buttons = []

        # Creating a list of all the buttons, for use in the for loop connecting them all to the same slot with different parameters.
        self.buttons = [self.ui.button00, self.ui.button01, self.ui.button02, self.ui.button10, self.ui.button11, self.ui.button12, self.ui.button20, self.ui.button21, self.ui.button22]
        for button in self.buttons:
            button.clicked.connect( lambda checked, button=button : self.pressed(button))

    def update_status(self):
        # Set label after turn
        if self.cross:
            self.ui.label.setText("Cross plays")
        else:
            self.ui.label.setText("Circle plays")
        # Check if board is full
        if len(self.pressed_buttons) >= 9:
            self.game_over = True
            self.ui.label.setText("Tie!")
        # Check if anyone has won
        if logic.check_for_wins() == "x":
            self.game_over = True
            self.ui.label.setText("Cross wins!")
        elif logic.check_for_wins() == "o":
            self.game_over = True
            self.ui.label.setText("Circle wins!")

    def pressed(self, button):
        # Check if the game is completed, and resets if so
        if self.game_over:
            self.clear()
            return # Without this the game would clear and the first turn would happen during the same click.
        # Don't allow plays on used spots
        if button not in self.pressed_buttons:
            if self.cross:
                button.setText("X")
                logic.x[self.buttons.index(button)] = 1
            else:
                button.setText("O")
                logic.o[self.buttons.index(button)] = 1
            # Switch turn
            self.cross = not self.cross
            self.pressed_buttons.append(button)
            self.update_status()

    def clear(self):
        # Remove button text
        for button in self.buttons:
            button.setText("")
        # Remove buttons from pressed list
        self.pressed_buttons = []
        # Clear logic engine
        logic.reset()
        # Setup label
        if self.cross:
            self.ui.label.setText("Cross begins")
        else:
            self.ui.label.setText("Circle begins")
        self.game_over = False


program = QApplication.instance()
if program == None:
    program = QApplication(sys.argv)
tictactoe = Tictactoe()
tictactoe.ui.show()
program.exec()
