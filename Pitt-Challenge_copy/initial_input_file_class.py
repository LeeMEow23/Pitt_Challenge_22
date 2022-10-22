import sys
from PyQt6 import QtWidgets, uic
from PIL import Image
from numpy import asarray
from image_load import image_load

global function_return

class initial_input_file(QtWidgets.QWidget):

    def __init__(self):
        super(initial_input_file, self).__init__()
        # Loads the UI from form.ui file
        uic.loadUi("initial_input_file_gui.ui", self)
        # Setting geometry, window title, showing gui
        self.setGeometry(100, 100, 400, 330)
        self.setWindowTitle("AccessRx GUI")
        self.img_array = 0
        self.send_image_button.clicked.connect(self.send_image_pressed)
        self.input = self.image_text_input

        self.show()

    def send_image_pressed(self):
        global function_return
        self.setGeometry(0, 0, 0, 0)
        function_return = image_load(self.input.toPlainText())
        print(function_return)
