import xlrd
#打开EXCEL文件
excel = xlrd.open_workbook('/杂/豆瓣电影Top250.xls')
#获取第一个sheet
sheet = excel.sheets()[0]
ls = []
for row_index in range(sheet.nrows):
    row_data = sheet.row_values(row_index)
    ls.append(row_data)
for line in ls[1:]:  # 跳过标题行
    # 提取line[0]
    value = str(int(line[0]))
    # 添加line[3]和line[4]
    value += " " + line[3] + " " + line[4]
    # 打印结果
    print(value)



