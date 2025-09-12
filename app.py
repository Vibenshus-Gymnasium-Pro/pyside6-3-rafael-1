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

        # Creating a list of all the buttons, for use in the for loop connecting them all to the same slot with different parameters. NOTE Not done
        # self.buttons = [self.ui.button00, self.ui.button01, self.ui.button02, self.ui.button10, self.ui.button11, self.ui.button12, self.ui.button20, self.ui.button21, self.ui.button22]
        self.buttons = {self.ui.button00: "00", self.ui.button01: "01", self.ui.button02: "02", self.ui.button10: 10, self.ui.button11: 11, self.ui.button12: 12, self.ui.button20: 20, self.ui.button21: 21, self.ui.button22: 22}
        for button in self.buttons:
            button.clicked.connect( lambda checked, button=button : self.pressed(button))

    def pressed(self, name):
        if self.cross == True:
            name.setText("X")
        else:
            name.setText("O")
        self.cross = not self.cross


program = QApplication.instance()
if program == None:
    program = QApplication(sys.argv)
tictactoe = Tictactoe()
tictactoe.ui.show()
program.exec()
