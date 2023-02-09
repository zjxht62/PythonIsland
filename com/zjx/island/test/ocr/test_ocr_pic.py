#!/usr/bin/env python3
# coding:utf-8
import os
import easyocr
from com.zjx.island.biz.ocr.ocr_pic import ocr_one_pic
from com.zjx.island.biz.leke.leke_biz import LekeClassTool

# 获取当前文件的绝对路径
ABS_PATH = os.path.dirname(os.path.realpath(__file__))
IMG_PATH = os.path.join(ABS_PATH, '../../../../../images/')


def test_ocr_one_pic():
    reader = easyocr.Reader(['ch_sim', 'en'])
    pic_path = os.path.join(IMG_PATH, 'leke2.jpg')
    result = ocr_one_pic(reader, pic_path)
    print(result)
    assert len(result) > 0

def test_leke_result():
    reader = easyocr.Reader(['ch_sim', 'en'])
    pic_path = os.path.join(IMG_PATH, 'leke2.jpg')
    result = ocr_one_pic(reader, pic_path)
    leke_class_tool = LekeClassTool(result)
    print(leke_class_tool.get_class_full_info())
