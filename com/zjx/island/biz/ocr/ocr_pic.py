#!/usr/bin/env python3
# coding:utf-8
import os
import easyocr
# 首次运行时若下载模型时提示ssl错误，加入以下两行再运行
#import ssl
#ssl._create_default_https_context = ssl._create_unverified_context

# 获取当前文件的绝对路径
# ABS_PATH = os.path.dirname(os.path.realpath(__file__))
# IMG_PATH = os.path.join(ABS_PATH, '../../../../../images/')
# reader = easyocr.Reader(['ch_sim', 'en'])
# pic_path = os.path.join(IMG_PATH, 'chinese.jpg')
# result = reader.readtext(pic_path)
# print(result)

def ocr_one_pic(reader, pic_path):
    return reader.readtext(pic_path)