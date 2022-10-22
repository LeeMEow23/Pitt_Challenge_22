import sys
from PyQt6 import QtWidgets, uic
from PIL import Image
from numpy import asarray

language = 0

class lang_input(QtWidgets.QWidget):

    def __init__(self):
        super(lang_input, self).__init__()
        self.lang_choice = 0
        # Loads the UI from form.ui file
        uic.loadUi("lang_input_gui.ui", self)
        # Setting geometry, window title, showing gui
        self.setGeometry(100, 100, 400, 330)
        self.setWindowTitle("AccessRx GUI")
        self.lang_select_box.addItems(["English", "Mandarin : 普通话", "Russian : Русский"])
        # Dealing with language selector bar, defining the input
        self.send_lang_button.clicked.connect(self.lang_define)
        self.show()

    def lang_define(self):
        global language
        self.setGeometry(0, 0, 0, 0)
        self.lang_choice = self.lang_select_box.currentText()
        print(self.lang_choice)
        language = self.lang_choice



    

        