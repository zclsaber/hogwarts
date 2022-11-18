import openpyxl

# 获取工作簿
book = openpyxl.load_workbook('params.xlsx')

# 获取活动工作表
sheet = book.active

# 获取单元格
a1 = sheet['A1'].value
print(a1)

c3 = sheet.cell(column=3, row=3).value
print(c3)

cells = sheet['A1':'C3']
print(type(cells), cells)

vals = []
for cell in cells:
    for c in cell:
        print(type(c), c)
        vals.append(c.value)
print(vals)