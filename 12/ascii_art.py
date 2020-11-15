# -*- coding: utf-8 -*- 
from PIL import Image
import os

CODE_LIB = r"@B%8&WM#ahdpmZOQLCJYXzcunxrjft/\|()1[]?-_+~<>i!I;:,    "
count = len(CODE_LIB)

def transform_ascii(image_file): 
    image_file = image_file.convert("L") 
    code_pic = '' 
    for h in range(0,image_file.size[1]):
        for w in range(0,image_file.size[0]): 
            gray = image_file.getpixel((w,h))
            code_pic = code_pic + CODE_LIB[int(((count-1)*gray)/256)]
        code_pic = code_pic + "\n" 
    return code_pic

def convert_image(fn, hratio=1.0, wratio=1.0):
    fp = open(fn,'rb')
    image_file = Image.open(fp)
    image_file=image_file.resize((int(image_file.size[0]*wratio), int(image_file.size[1]*hratio)))
    print(u'Size info:',image_file.size[0],' ',image_file.size[1],' ')
    tmp = open('result.txt','w')
    trans_data = transform_ascii(image_file)
    print(trans_data)
    tmp.write(trans_data)
    tmp.close()
