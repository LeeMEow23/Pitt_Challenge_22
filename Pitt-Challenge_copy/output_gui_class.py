import sys
from tkinter import N
from PyQt6 import QtWidgets, uic
from PIL import Image
from numpy import asarray
from med_input_gui_class import *
from OCR_2 import *

full_output = {"medication_name": "", "medication_info": "", "Monday": "", "Tuesday": "", "Wednesday": "", "Thursday": "", "Friday": "", "Saturday": "", "Sunday": ""}
full_output["Monday"] = str(med_freq_select)
full_output["Tuesday"] = str(med_freq_select)
full_output["Wednesday"] = str(med_freq_select)
full_output["Thursday"] = str(med_freq_select)
full_output["Friday"] = str(med_freq_select)
full_output["Saturday"] = str(med_freq_select)
full_output["Sunday"] = str(med_freq_select)
full_output["medication_name"] = str(med_text_value)
full_output["medication_info"] = str(med_dosage_select)

full_output["medication_name"] = returned_array_to_med_gui[0]
full_output["medication_info"] = returned_array_to_med_gui[3] + "Take one tablet by mouth at bedtime"





class output(QtWidgets.QWidget):

    def __init__(self):
        self.med_text_input = 0
        self.med_dosage_select = 0
        self.med_freq_select = 0
        super(output, self).__init__()
        # Loads the UI from form.ui file
        uic.loadUi("output_gui.ui", self)
        # Setting geometry, window title, showing gui
        self.setGeometry(100, 100, 390, 330)
        self.setWindowTitle("AccessRx GUI")
        # Setting output box value
        data = ["Name: " + full_output['medication_name'], "Info: " + full_output["medication_info"], "*SCHEDULE*", 
        "Monday: " + full_output["Monday"], "Tuesday: " + full_output["Tuesday"], "Wednesday: " + full_output["Wednesday"], "Thursday: " + full_output["Thursday"],
        "Friday: " + full_output['Friday'], "Saturday: " + full_output["Saturday"], "Sunday: " + full_output["Sunday"]]
        self.output_box.setText("\n".join(data))
        self.output_exit_button.clicked.connect(self.sys_exit_func)

        self.show()

    def sys_exit_func(self):
        self.setGeometry(0, 0, 0, 0)
        print("System has completed a cycle.")

        
        
