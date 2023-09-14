import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QSize, Qt

# Only needed for access to command line arguments
import sys

from PyQt6.QtWidgets import QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("SB App")
        self.button = QPushButton("Press Me!")
        
        # self.setFixedSize(QSize(400, 300))
        self.setCentralWidget(self.button)
        
        # button.setCheckable(True)
        self.button.clicked.connect(self.the_button_was_clicked)
        # button.clicked.connect(self.the_button_was_toggled)
        
    def the_button_was_clicked(self):
        self.button.setText("You already clicked me.")
        self.button.setEnabled(False)
        self.setWindowTitle("SB App(2)")

    # def the_button_was_toggled(self, checked):
    #     print("Checked?", checked)
        
# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
# window = QWidget()
# window = QPushButton("Push Me")
window = MainWindow()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()
