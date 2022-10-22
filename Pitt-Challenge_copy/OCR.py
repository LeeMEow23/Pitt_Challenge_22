from paddleocr import PaddleOCR, draw_ocr 
from matplotlib import pyplot as plt 
import cv2 
import os 
import copy
import numpy as np

# main_dir = '/Users/wanglimiao/Desktop'
# ocr = PaddleOCR(lang='en')
# img_path = os.path.join(main_dir, 'drug.jpg')
# ocr = PaddleOCR(use_angle_cls=True, lang='en')
img_path = '//Users//wanglimiao//Desktop//drug.jpg'
img = cv2.imread(img_path)
print(img)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# plt.figure(figsize=(15,15))
# annotated = draw_ocr(img, boxes, texts, scores, font_path=font_path)
# plt.imshow(annotated)
# result = ocr.ocr(img_path, cls=True)
# for line in result:
#     print(line)

# # draw result
# from PIL import Image
# result = result[0]
# image = Image.open(img_path).convert('RGB')
# boxes = [line[0] for line in result]
# txts = [line[1][0] for line in result]
# scores = [line[1][1] for line in result]
# im_show = draw_ocr(image, boxes, txts, scores, font_path='/path/to/PaddleOCR/doc/fonts/simfang.ttf')
# im_show = Image.fromarray(im_show)
# im_show.save('result.jpg')