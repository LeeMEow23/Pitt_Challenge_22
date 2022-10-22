import sys
from PyQt6 import QtWidgets, uic
from PIL import Image
from numpy import asarray
from OCR_2 import *

med_text_value = "Amitryp"
med_dosage_select = "100 mg"
med_freq_select = "3 times a day"

class med_input(QtWidgets.QWidget):

    def __init__(self):
        super(med_input, self).__init__()
        # Loads the UI from form.ui file
        uic.loadUi("med_input_gui.ui", self)
        # Setting geometry, window title, showing gui
        self.setGeometry(100, 100, 400, 295)
        self.setWindowTitle("AccessRx GUI")
        # self.holder = self.med_input_subheader.text()
        # print("AAA",self.holder)
        # self.med_input_subheader.setText(translate(self.holder))
        # self.holder = self.error_label.text()
        # self.error_label.setText(translate(self.holder))
        # self.holder = self.error_label2.text()
        # self.error_label2.setText(translate(self.holder))
        # self.holder = self.med_dosage_label.text()
        # self.med_dosage_label.setText(translate(self.holder))
        # self.holder = self.med_freq_label.text()
        # self.med_freq_label.setText(translate(self.holder))
        # Sending medical information inputs to definer function
        self.med_input_send.clicked.connect(self.send_med_inputs)
        self.med_dosage_input.addItems(["10mg", "20mg", "30mg", "40mg", "50mg", "60mg", "70mg", "80mg", "90mg", "100mg"])
        #self.med_freq_input.addItems([translate("Once a day, morning"), translate("Once a day, bedtime"), translate("Twice a day"), translate("Three times a day"), translate("As needed")])
        self.med_freq_input.addItems(["Once a day, morning", "Once a day, bedtime", "Twice a day", "Three times a day", "As needed"])
        self.show()

    def send_med_inputs(self):
        self.geometry(0, 0, 0, 0)
        global med_text_value
        global med_dosage_select
        global med_freq_select
        med_text_value = self.med_text_input.toPlainText()
        med_dosage_select = str(self.med_dosage_input.currentText())
        med_freq_select = str(self.med_freq_input.currentText())
        print(med_text_value)
        print(med_dosage_select)
        print(med_freq_select)

        
        
