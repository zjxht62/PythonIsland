import openpyxl

# 定义最终需要映射的表


{
    "编号": {
        'type': 'default'
    },
    '姓名': {
        'type': 'default'
    },
    '总分': {
        'type': 'default'
    },
    'T1': {
        'type': 'int',
        'contains': []
    }
}

# 打开一个已存在的工作簿
workbook = openpyxl.load_workbook('初三期末(历史)-九年级1班.xlsx')

# 获取默认的工作表
sheet = workbook.active

# 读取单元格A1的数据
data = sheet['A1'].value
print(data)

origin_rows = []
for row in sheet.iter_rows(min_row=2, values_only=True):
    origin_rows.append(row)

print(origin_rows)

l1: tuple = origin_rows[0]
print(l1.index('1'))
result_rows = []
# 关闭工作簿
workbook.close()


def select_need_column(origin_rows, column_names):
    # 指定要选择的下标位置
    selected_indices = []
    selected_rows = []

    head_line = origin_rows[0]
    for cn in column_names:
        index = head_line.index(cn)
        selected_indices.append(index)
    for row in origin_rows:
        selected_rows.append(tuple(row[i] for i in selected_indices))

    return selected_rows


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

column_names = ['姓名', '班内学号', '单选题', '31(1)', '31(2)', '31(3)', '31(4)', '32(1)', '32(2)', '32(3)',
                '33(1)', '33(2)', '33(3)', '33(4)', '34(1)', '34(2)', '34(3)', '34(4)']
# 按列选出需要的列
selected_columns = (select_need_column(origin_rows, column_names))


def sort_by_column(origin_rows, column_name):
    column_index = origin_rows[0].index(column_name)
    sorted_list = sorted(origin_rows, key=lambda x: x[column_index])
    return sorted_list


# 按指定列排序，比如学号
print(sort_by_column(origin_rows, '班内学号'))
