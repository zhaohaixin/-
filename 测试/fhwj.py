import os
import csv
from collections import Counter

import xlrd


def open_excel(fileofexcel):
    try:
        data = xlrd.open_workbook(fileofexcel)
        return data
    except Exception as e:
        print(str(e))


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

count=Counter(sum_list)
#按值排序
sort_list=sorted(count.items(),key = lambda x:x[1],reverse = True)
sort_list.insert(0,('群号','加入人数'))
with open('碰撞值.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    # 还可以写入多行
    writer.writerows(sort_list)