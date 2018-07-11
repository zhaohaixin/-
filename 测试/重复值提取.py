def open_excel(fileofexcel):
    try:
        data = xlrd.open_workbook(fileofexcel)
        return data
    except Exception as e:
        print(str(e))


import os

import xlrd

file_xlsx = []
temp_dict = {}
sum_list = []
############----获取指定目录下的xlsx文件数和路径地址----#################
# 当前文件的路径
root_path = os.getcwd()
file = os.listdir(root_path)
for x in file:
    newDir = os.path.join(root_path, x)
    if os.path.isfile(newDir):
        # 指定要的文件类型
        if os.path.splitext(newDir)[1] == '.xlsx':
            file_xlsx.append(newDir)
number = len(file_xlsx)
# 获取每个表格的数据
for x in file_xlsx:
    temp_list = open_excel(x).sheet_by_name('Sheet1').col_values(0)
    temp_list = temp_list[1:]
    temp_list = list(map(int, temp_list))
    temp_dict.update({os.path.basename(x): temp_list})
    sum_list += list(set(temp_list))


# mylist = [1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# myset = set(mylist)  # myset是另外一个列表，里面的内容是mylist里面的无重复 项
# for item in myset:
#     print("the %d has found %d" % (item, mylist.count(item)))
