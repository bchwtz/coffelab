# gui.py
"""Main window-style application."""

from curses import window
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from functools import partial
from beverage import Beverage

DISPLAY_HEIGHT = 35
BUTTON_HEIGHT = 40
BUTTON_WIDTH = 100
ERROR_MSG = "ERROR"

bev = Beverage("Espresse", size="M")
bev.extrashot = True

def evaluateExpression(record):
    return "YOLO:"

class PyCalc:
    """PyCalc's controller class."""

    def __init__(self, model, view):
        self._evaluate = model
        self._view = view
        self._view._createStatusBar()
        self._connectSignalsAndSlots()

    def _calculateResult(self):
        #result = self._evaluate(expression=self._view.displayText())
        result = str(bev.price)
        self._view.setDisplayText(result)
        #bev.type = "Koffee"
        self._view._createStatusBar()

    def _setBeverage(self):
        bev.type = "Cappucchino"

    def _buildExpression(self, subExpression):
        if self._view.displayText() == ERROR_MSG:
            self._view.clearDisplay()
        expression = self._view.displayText() + subExpression
        self._view.setDisplayText(expression)

    def _connectSignalsAndSlots(self):
        for keySymbol, button in self._view.buttonMap.items():
                    if keySymbol not in {"=", "C"}:
                        button.clicked.connect(
                            partial(self._buildExpression, keySymbol)
                        )
        
        self._view.buttonMap["Espresso"].clicked.connect(self._calculateResult)
        self._view.buttonMap["Cappucchino"].clicked.connect(self._setBeverage)
        #self._view.buttonMap["Cappucchino"].clicked.connect(self._view._createStatusBar())

        #self._view.display.returnPressed.connect(self._calculateResult)
        #self._view.buttonMap["C"].clicked.connect(self._view.clearDisplay)
       #None



class Window(QMainWindow):

    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("QMainWindow")
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)
        self._createDisplay()
        self._createButtons()
        self._createMenu()
        self._createToolBar()
        self._createStatusBar()

    def _createDisplay(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(DISPLAY_HEIGHT)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)

    def _createButtons(self):
            # Beverages Buttons
            self.buttonMap = {}
            beveragesLayout = QHBoxLayout()
            keys = list(Beverage.types.keys())

            for key in list(Beverage.types.keys()):
                self.buttonMap[key] = QPushButton(key)
                self.buttonMap[key].setFixedSize(BUTTON_WIDTH, BUTTON_HEIGHT)
                beveragesLayout.addWidget(self.buttonMap[key])
                
            self.generalLayout.addLayout(beveragesLayout)

            # Complete Order Buttons
            finishLayout = QHBoxLayout()
            finishLayout.addWidget(QPushButton("X"))
            finishLayout.addWidget(QPushButton("Print"))
            self.generalLayout.addLayout(finishLayout)

    def setDisplayText(self, text):
            """Set the display's text."""
            self.display.setText(text)
            self.display.setFocus()

    def displayText(self):
            """Get the display's text."""
            return self.display.text()

    def clearDisplay(self):
            """Clear the display."""
            self.setDisplayText("")

    def _createMenu(self):
        menu = self.menuBar().addMenu("&Menu")
        menu = self.menuBar().addMenu("&TEST")
        menu.addAction("&Exit", self.close)

    def _createToolBar(self):
        tools = QToolBar()
        tools.addAction("Exit", self.close)
        self.addToolBar(tools)

    def _createStatusBar(self):
        status = QStatusBar()
        #status.showMessage("I'm the Status Bar")
        status.showMessage(str(bev))
        self.setStatusBar(status)

def main():
    """Main function."""
    app = QApplication([])
    window = Window()
    window.show()
    PyCalc(model=evaluateExpression, view=window)
    sys.exit(app.exec())

if __name__ == "__main__":
    main()


