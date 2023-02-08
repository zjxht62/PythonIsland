#!/usr/bin/env python3
# coding:utf-8
import os
import easyocr
from com.zjx.island.biz.ocr.ocr_pic import ocr_one_pic

# 获取当前文件的绝对路径
ABS_PATH = os.path.dirname(os.path.realpath(__file__))
IMG_PATH = os.path.join(ABS_PATH, '../../../../../images/')


def test_ocr_one_pic():
    reader = easyocr.Reader(['ch_sim', 'en'])
    pic_path = os.path.join(IMG_PATH, 'WechatIMG300.png')
    result = ocr_one_pic(reader, pic_path)
    print(result)
    assert len(result) > 0
