#!/usr/bin/env python3
# coding:utf-8
import os
import easyocr

# 获取当前文件的绝对路径
ABS_PATH = os.path.dirname(os.path.realpath(__file__))
IMG_PATH = os.path.join(ABS_PATH, '../../../../../images/')
reader = easyocr.Reader(['ch_sim', 'en'])
pic_path = os.path.join(IMG_PATH, 'chinese.jpg')
result = reader.readtext(pic_path)
print(result)