from paddleocr import PaddleOCR, draw_ocr 
from matplotlib import pyplot as plt 
import cv2 
import os 
import copy
import numpy as np
import sys
import requests
import  json
import pandas as pd
import http.client
import ast

def translate(med_name):
    conn = http.client.HTTPSConnection("nlp-translation.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': "c1aaffde26msh23458fde187178ep156b18jsn94e7ce0b0855",
        'X-RapidAPI-Host': "nlp-translation.p.rapidapi.com"
        }

    URL = '/v1/translate?text='
    API = URL + med_name + '&to=zh-CN&from=en'
    #print(API)
    #conn.request("GET", "/v1/translate? text=amitriptyline &to=zh-CN&from=en", headers=headers)
    conn.request("GET", API, headers=headers)
    res = conn.getresponse()
    data = res.read()
    data1 = data.decode("utf-8")
    data2 = ast.literal_eval(data1)
    result = list((data2['translated_text']).values())[0]
    return result
    #print(result)
    # data1 = data.decode("utf-8")
    # result = data["translated_text"]
    #print(result)

#{"status":200,"from":"en","to":"zh-CN","original_text":"amitriptyline",
#"translated_text":{"zh-CN":"阿米替林"},"translated_characters":13}




# # main_dir = '/Users/wanglimiao/Desktop'
def read_drug_label(img_file_name, lang = 'en'):
    ocr = PaddleOCR(lang = lang, use_angle_cls=True)
    print('start\n')

    img_path = os.path.join('.', img_file_name)
    # print(img_path)
    read_result = ocr.ocr(img_path)[0]
    # print(read_result)
    result = []

    for res in read_result:
        # print(res[1][0])
        s = ''
        s = s + res[1][0]
        result += [s]
    return result

# print(read_drug_label('Try2.JPG'))


#OpenFDA
def get_med_data(med_name):
    API  = 'https://api.fda.gov/drug/label.json?search='
    drug    = 'openfda.brand_name=' + med_name
    URL     = API + drug
    result = []
    try:
        data  = requests.get(URL).json()['results'][0]['indications_and_usage']
        if med_name != 'AMITRIPTYLINE HCL 10':
            #print('Not a term')
            pass
        else:
            #print(med_name)
            result.append(data)
            
    except:
        #print('Not a term')
        pass
    return result


#OpenFDA
def get_med_data2(med_name):
    API  = 'https://api.fda.gov/drug/label.json?search='
    drug    = 'openfda.brand_name=' + med_name
    URL     = API + drug
    result = []
    name = ""
    try:
        data1  = requests.get(URL).json()['results'][0]['information_for_patients']
        if med_name != 'AMITRIPTYLINE HCL 10':
            #print('Not a term')
            pass
        else:
            result.append(data1)  
            name = med_name   
    except:
        #print('Not a term')
        pass
    return (result, name)


#
def get_drug_name(term_list):
    result = []
    name = ""
    for term in term_list:
        check = get_med_data(term)
        check2, cur_name =get_med_data2(term)
        
        if check:
            result += [check][0]
            result += [check2][0]
            name = cur_name
        
    #print(result[1][0])
    return (result[1][0], name)


drug_dict = dict({"AMITRIPTYLINE HCL 10": ["Take one tablet by mouth at bedtime", "No known interaction", "Do not crush this tablet"],
"Benzonatate 100 mg": ["Take 2 pills, twice a day", "No known interaction", "Do not crush this tablet"], 
"Montelukast sod 10 mg": ["Take one tablet by mouth at bedtime", "No known interaction", "Do not crush this tablet"]})


def get_info(name, drug_dict):
    info = drug_dict[name]
    dosage = info[0]
    interaction = info[1]
    how_to = info[2]
    return (name, dosage, interaction, how_to)

returned_array_to_med_gui = get_info("AMITRIPTYLINE HCL 10", drug_dict)


# term_list = read_drug_label('Try2.JPG')
# more_info, name = get_drug_name(term_list)
# dosage, interaction, how_to = get_info(name, drug_dict)












# def get_med_data(med_name):
#     count = 0
#     result = []
#     API  = 'https://api.fda.gov/drug/label.json?search='
#     #date    = 'receivedate:[20180101+TO+20201022]'
#     #country = 'occurcountry:"US"'
#     drug    = 'openfda.brand_name=' + "\"" + med_name + "\""
#     #data    = 'count=receivedate'
#     URL     = API + drug
#     # print(URL)
#     # try:
#     data  = requests.get(URL).json()['results'][0]['indications_and_usage']
#     print(data)
#     #     result.append(data)
#     # except:
#     #     count +=1 
#     #     if count == len(med_name):
#     #         print('Not a term')
#     # return result

# get_med_data('AMITRIPTYLINE HCL 10')
#   #https://api.fda.gov/drug/label.json?search=openfda.brand_name="AMITRIPTYLINE HCL 10"
#   #https://api.fda.gov/drug/label.json?search=openfda.brand_name:"AMITRIPTYLINE HCL 10"
#     #fda_df  = pd.read_json(json.dumps(data))
    

#     #print(data)

# #get_med_data("Alison")

# #term_list = read_drug_label('Try2.JPG')
# def get_drug_name(term_list):
#     result = []
#     for term in term_list:
#         check = get_med_data(term)
#         if check:
#             result += [check]
#     print(result)
#     return result


# term_list = read_drug_label('Try2.JPG') 
# ## ['UPMC', 'R#6537225', 'RPh', 'JULIUS AROLOVITCH', 'TAKE ONE TABLET BYM', 
# ## 'AMITRIPTYLINE HCL 10', 'MAY CAUSE', 'HAYARE']
# get_drug_name(term_list)




# list_terms = read_drug_label('Try.PNG')
# for term in list_terms:







# out_path = './output_images'
# font = './Helvetica-Bold-Font.ttf'

# # save_ocr(img_path, out_path, result, font)

# boxes = [res[0] for res in result] 
# texts = [res[1][0] for res in result]
# scores = [res[1][1] for res in result]
# font_path = os.path.join('PaddleOCR', 'doc', 'fonts', 'latin.ttf')

# img = cv2.imread('./1.jpg')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# plt.figure(figsize=(15,15))
# annotated = draw_ocr(img, boxes, texts, scores, font_path=font_path) 
# plt.imshow(annotated)
# # # plt.figure(figsize=(15,15))
# # # annotated = draw_ocr(img, boxes, texts, scores) 
# # # plt.imshow(annotated)

# cv2.imshow('image',img)
# cv2.waitKey()

# def save_ocr(img_path, out_path, result, font):
#     save_path = os.path.join(out_path, img_path.split('/')[-1] + 'output')
#     image = cv2.imread(img_path)
#     boxes = [line[0] for line in result]
#     txts = [line[1][0] for line in result]
#     scores = [line[1][1] for line in result]
    
#     im_show = draw_ocr(image, boxes, txts, scores, font_path=font)
    
#     cv2.imwrite(save_path, im_show)
    
#     img = cv2.cvtColor(im_show, cv2.COLOR_BGR2RGB)
#     plt.imshow(img)