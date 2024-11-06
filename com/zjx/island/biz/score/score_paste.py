import openpyxl
from yaml_util import get_all_from_columns, load_yaml


# 从第n行开始获取数据
def get_rows_from_n_start(path, n=1):
    # 打开一个已存在的工作簿
    workbook = openpyxl.load_workbook(path)

    # 获取默认的工作表
    sheet = workbook.active

    rows = []
    for row in sheet.iter_rows(min_row=n, values_only=True):
        rows.append(row)

    # 关闭工作簿
    workbook.close()
    return rows

# 获取一个工作表所有sheet页的数据，按sheet页排成一个嵌套列表
def get_all_rows_without_first_from_all_sheet(path):
    # 打开一个已存在的工作簿
    workbook = openpyxl.load_workbook(path)

    all_rows_data = []

    for sheet_name in workbook.sheetnames:
        sheet = workbook[sheet_name]
        origin_rows = []
        for row in sheet.iter_rows(min_row=2, values_only=True):
            origin_rows.append(row)
        all_rows_data.append(origin_rows)

    # 关闭工作簿
    workbook.close()
    return all_rows_data

if __name__ == '__main__':
    result_template_file = './粘贴结果模板.xlsx'
    auto_result_file = './自动合分结果.xlsx'

    head_rows = get_rows_from_n_start(result_template_file)

    output_rows = []

    all_auto_result_rows = []
    for r in get_all_rows_without_first_from_all_sheet(auto_result_file):
        all_auto_result_rows+=r

    for m in head_rows:
        for r in all_auto_result_rows:
            # if r[1] in m:
            #     print(m+r)
            #     head_rows.remove(m)
            #     all_auto_result_rows.remove(r)
            # else:
            #     print(m)
            if m[1] == r[1]:
                output_rows.append(m+r)


    # 创建保存结果的工作表
    workbook = openpyxl.Workbook()
    workbook.remove(workbook.active)
    new_sheet = workbook.create_sheet('待复制')
    for r in output_rows:
        new_sheet.append(r)

    workbook.save('待复制结果.xlsx')
