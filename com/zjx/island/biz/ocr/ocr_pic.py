#!/usr/bin/env python3
# coding:utf-8
import os
import easyocr


# 首次运行时若下载模型时提示ssl错误，加入以下两行再运行
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

# 获取当前文件的绝对路径
# ABS_PATH = os.path.dirname(os.path.realpath(__file__))
# IMG_PATH = os.path.join(ABS_PATH, '../../../../../images/')
# reader = easyocr.Reader(['ch_sim', 'en'])
# pic_path = os.path.join(IMG_PATH, 'chinese.jpg')
# result = reader.readtext(pic_path)
# print(result)

def ocr_one_pic(reader, pic_path):
    return reader.readtext(pic_path)


if __name__ == '__main__':
    # 获取当前文件的绝对路径
    ABS_PATH = os.path.dirname(os.path.realpath(__file__))
    IMG_PATH = os.path.join(ABS_PATH, '../../../../../images/')
    reader = easyocr.Reader(['ch_sim', 'en'])
    pic_path = os.path.join(IMG_PATH, 'leke2.jpg')
    result = ocr_one_pic(reader, pic_path)
    class_name_result = [r for r in result if (200 < r[0][0][0] < 350) and (300 < r[0][1][0] - r[0][0][0])]
    class_time_result = [r for r in result if (245 < r[0][0][0] < 250) and (195 < r[0][1][0] - r[0][0][0] < 205)]
    class_teacher_result = [r for r in result if (465 < r[0][0][0] < 470) and (75 < r[0][1][0] - r[0][0][0])]
    class_status_result = [r for r in result if (1023 < r[0][0][0] < 1028) and (70 < r[0][1][0] - r[0][0][0])]
    for r in class_name_result:
        print(r)
    print("换行")
    for r in class_time_result:
        print(r)
    print("换行")
    for r in class_teacher_result:
        print(r)
    print("换行")
    for r in class_status_result:
        print(r)
    print("换行")
    for r in result:
        print(r)
