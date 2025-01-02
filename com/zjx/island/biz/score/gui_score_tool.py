import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import shutil
import openpyxl
from enum import Enum
from pathlib import Path

from com.zjx.island.biz.score.path_util import get_config_path, create_results_folder
from com.zjx.island.biz.score.yaml_util import load_yaml
from com.zjx.island.biz.score.score_statistics import get_all_from_columns, get_all_rows_without_first_from_all_sheet, \
    get_all_rows_without_first, select_need_column, convert_to_target_column, get_rows_from_n_start


class Subject(Enum):
    YUWEN = 1
    SHUXUE = 2
    YINGYU = 3
    WULI = 4
    HUAXUE = 5
    SHENGWU = 6
    LISHI = 7
    DILI = 8
    ZHENGZHI = 9


def select_files():
    files = filedialog.askopenfilenames(title="选择多个文件")
    if files:
        selected_files.clear()
        selected_files.extend(files)
        update_file_list_display()
    else:
        messagebox.showwarning("警告", "请至少选择一个文件！")


def update_file_list_display():
    file_list_display.delete(1.0, tk.END)
    for file in selected_files:
        file_list_display.insert(tk.END, file + "\n")


def generate_result_files():
    global output_file_path
    auto_result_file_name = f'自动合分结果-{selected_subject.name}.xlsx'

    if not selected_subject:
        messagebox.showwarning("警告", "没有选择科目！")
        return

    if not selected_files:
        messagebox.showwarning("警告", "没有选择文件！")
        return

    # 创建输出文件目录
    output_dir = create_results_folder('output_files')
    output_file_path = output_dir / auto_result_file_name

    workbook = openpyxl.Workbook()
    workbook.remove(workbook.active)

    for file in selected_files:

        # 首先去掉顶部标题
        origin_rows = get_all_rows_without_first(file)
        selected_rows = select_need_column(origin_rows, get_all_from_columns(selected_subject))
        result_rows = convert_to_target_column(selected_rows, load_yaml(selected_subject))
        # 按学号排序
        sorted_list = sorted(result_rows, key=lambda x: x[0])
        sorted_list.insert(0, sorted_list.pop())

        for r in sorted_list:
            print(r)

        new_sheet = workbook.create_sheet(title=str(file).split('.')[0].split('-')[1])

        # 将数据写入新的工作表
        for row_data in sorted_list:
            new_sheet.append(row_data)

    workbook.save(output_file_path)

    messagebox.showinfo("成功", f"生成了新文件:{output_file_path.name}，保存在 output_files 目录下")


def generate_copy_files():
    auto_to_copy_file_name = f'待复制结果-{selected_subject.name}.xlsx'
    copy_template_file_name = '粘贴结果模板.xlsx'

    # 读取模板文件
    template_file = get_config_path('templates', copy_template_file_name)  # 假设模板文件为 template.txt
    if not template_file.exists():
        messagebox.showerror("错误", "模板文件不存在！")
        return

    # 结果文件路径
    auto_result_file = f'自动合分结果-{selected_subject.name}.xlsx'
    output_dir = create_results_folder('output_files')
    auto_result_file_path = output_dir / auto_result_file
    auto_to_copy_file_path = output_dir / auto_to_copy_file_name

    # 按照粘贴模板生成结果
    head_rows = get_rows_from_n_start(template_file)

    output_rows = []

    all_auto_result_rows = []
    for r in get_all_rows_without_first_from_all_sheet(auto_result_file_path):
        all_auto_result_rows += r

    for m in head_rows:
        for r in all_auto_result_rows:
            # if r[1] in m:
            #     print(m+r)
            #     head_rows.remove(m)
            #     all_auto_result_rows.remove(r)
            # else:
            #     print(m)
            if m[1] == r[1]:
                output_rows.append(m + r)

    # 创建保存结果的工作表
    workbook = openpyxl.Workbook()
    workbook.remove(workbook.active)
    new_sheet = workbook.create_sheet('待复制')
    for r in output_rows:
        new_sheet.append(r)

    workbook.save(auto_to_copy_file_path)

    messagebox.showinfo("成功", f"生成了新文件:{auto_to_copy_file_path.name}，保存在 output_files 目录下")



def on_combobox_select(event):
    global selected_subject
    """当下拉框选择项改变时触发的事件"""
    selected_value = combobox.get()  # 获取当前选中的值
    if selected_value == '语文':
        selected_subject = Subject.YUWEN
    elif selected_value == '数学':
        selected_subject = Subject.SHUXUE
    elif selected_value == '英语':
        selected_subject = Subject.YINGYU
    elif selected_value == '物理':
        selected_subject = Subject.WULI
    elif selected_value == '化学':
        selected_subject = Subject.HUAXUE
    elif selected_value == '生物':
        selected_subject = Subject.SHENGWU
    elif selected_value == '历史':
        selected_subject = Subject.LISHI
    elif selected_value == '地理':
        selected_subject = Subject.DILI
    elif selected_value == '政治':
        selected_subject = Subject.ZHENGZHI
    print(f"选中的值: {selected_subject}")


def main():
    global file_list_display, selected_files, combobox, selected_subject
    selected_files = []
    selected_subject = None

    root = tk.Tk()
    root.title("合分小助手")
    root.geometry("500x400")

    # 创建下拉选择框（Combobox）
    options = ["语文", "数学", "英语", "物理", "化学", "生物", "历史", "地理", "生物"]
    combobox = ttk.Combobox(root, values=options)
    combobox.set("请选择学科")  # 设置默认提示文字
    combobox.bind("<<ComboboxSelected>>", on_combobox_select)
    combobox.pack(pady=20)

    select_button = tk.Button(root, text="选择文件", command=select_files)
    select_button.pack(pady=10)

    generate_button = tk.Button(root, text="生成合分结果文件", command=generate_result_files)
    generate_button.pack(pady=10)

    generate_button = tk.Button(root, text="生成可粘贴文件", command=generate_copy_files)
    generate_button.pack(pady=10)

    file_list_display = tk.Text(root, height=15, width=60)
    file_list_display.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
