from PIL import Image
from numpy import asarray
from PyQt6 import QtWidgets, uic
from OCR_2 import *

def image_load(file_name):
    global img_array
    img_file = Image.open(file_name)
    img_matrix = asarray(img_file)
    img_matrix = img_matrix[:, :, 0]
    img_array = img_matrix
    print(img_array)

    term_list = read_drug_label(file_name)

    more_info, name = get_drug_name(term_list)
    name, dosage, interaction, how_to = get_info(name, drug_dict)

    returned_array = [name, dosage, interaction, how_to]
    return returned_array



