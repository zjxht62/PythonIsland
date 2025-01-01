import openpyxl
from yaml_util import get_all_from_columns, load_yaml
from score_statistics import get_all_rows_without_first_from_all_sheet,get_rows_from_n_start


if __name__ == '__main__':
    result_template_file = 'templates/粘贴结果模板.xlsx'
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
