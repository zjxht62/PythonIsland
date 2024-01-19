import openpyxl
from yaml_util import get_all_from_columns, load_yaml


def get_all_rows_without_first(path):
    # 打开一个已存在的工作簿
    workbook = openpyxl.load_workbook(path)

    # 获取默认的工作表
    sheet = workbook.active

    origin_rows = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        origin_rows.append(row)

    # 关闭工作簿
    workbook.close()
    return origin_rows

def select_need_column(origin_rows, column_names):
    # 指定要选择的下标位置
    selected_indices = []
    selected_rows = []

    head_line = origin_rows[0]
    # 根据列名找出要筛选的下标
    for cn in column_names:
        index = head_line.index(cn)
        selected_indices.append(index)
    for row in origin_rows:
        selected_rows.append(tuple(row[i] for i in selected_indices))
    # 排除学号为空以及为-的
    selected_rows_without_none = [r for r in selected_rows if r[0] is not None and r[0] != '-']
    return selected_rows_without_none

def convert_to_target_column(origin_rows, column_mapping):
    result_rows = []
    # 添加表头
    result_rows.append(tuple([m['target'] for m in column_mapping]))
    print(result_rows)
    head_line = origin_rows[0]

    for m in column_mapping:
        target_column_name = m['target']
        from_column_name_list = m['from']
        m['from_index'] = []
        for c in from_column_name_list:
            m['from_index'].append(head_line.index(c))


    for r in origin_rows[1:]:
        # 每个结果行作为list存储
        single_result_row_list = []
        for m in column_mapping:
            value = 0
            if len(m['from_index']) >1:
                for i in m['from_index']:
                    if r[i] == '-':
                        value = '-'
                        break
                    else:
                        value += r[i]
            else:
                value = r[m['from_index'][0]]
            single_result_row_list.append(value)
        print(single_result_row_list)

# original_tuple = (1, 2, 3, 4, 5, 6)
#
# # 指定要选择的下标位置
# selected_indices = (0, 2, 4)
#
# # 使用切片生成新的元组
# new_tuple = tuple(original_tuple[i] for i in selected_indices)
#
# # 打印新的元组
# print(new_tuple)
#
# column_names = ['姓名', '班内学号', '单选题', '31(1)', '31(2)', '31(3)', '31(4)', '32(1)', '32(2)', '32(3)',
#                 '33(1)', '33(2)', '33(3)', '33(4)', '34(1)', '34(2)', '34(3)', '34(4)']
# # 按列选出需要的列
# selected_columns = (select_need_column(origin_rows, column_names))
#
#
# def sort_by_column(origin_rows, column_name):
#     column_index = origin_rows[0].index(column_name)
#     sorted_list = sorted(origin_rows, key=lambda x: x[column_index])
#     return sorted_list
#
#
# # 按指定列排序，比如学号
# print(sort_by_column(origin_rows, '班内学号'))


if __name__ == '__main__':
    origin_rows = get_all_rows_without_first('初三期末(历史)-九年级1班.xlsx')
    selected_rows = select_need_column(origin_rows, get_all_from_columns())
    print(selected_rows)
    convert_to_target_column(selected_rows, load_yaml())
