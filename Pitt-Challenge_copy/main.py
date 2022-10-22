import sys
from PyQt6 import QtWidgets
from numpy import asarray
from image_load import *
from initial_input_file_class import initial_input_file
from med_input_gui_class import med_input
from lang_input_file_class import lang_input
from output_gui_class import output


app4 = QtWidgets.QApplication(sys.argv)
output_info = output()

# app3 = QtWidgets.QApplication(sys.argv)
# med_input_info = med_input()

app2 = QtWidgets.QApplication(sys.argv)
input_file = initial_input_file()

app = QtWidgets.QApplication(sys.argv)
lang_input_file = lang_input()

sys.exit(app4.exec())