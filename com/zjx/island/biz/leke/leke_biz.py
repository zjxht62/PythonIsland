#!/usr/bin/env python3
# coding:utf-8
class LekeClassTool:
    def __init__(self, ocr_result):
        self.ocr_result = ocr_result

    def get_class_name_result(self):
        return [r[1] for r in self.ocr_result if (200 < r[0][0][0] < 350) and (300 < r[0][1][0] - r[0][0][0])]

    def get_class_time_result(self):
        return [r[1] for r in self.ocr_result if (245 < r[0][0][0] < 250) and (195 < r[0][1][0] - r[0][0][0] < 205)]

    def get_class_teacher_result(self):
        return [r[1] for r in self.ocr_result if (465 < r[0][0][0] < 470) and (75 < r[0][1][0] - r[0][0][0])]

    def get_class_status_result(self):
        return [r[1] for r in self.ocr_result if (1023 < r[0][0][0] < 1028) and (70 < r[0][1][0] - r[0][0][0])]

    def get_class_full_info(self):
        return list(zip(self.get_class_name_result(), self.get_class_time_result(), self.get_class_teacher_result(), self.get_class_status_result()))