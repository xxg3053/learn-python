#打开excel
import xlrd

def excel_base():
    wb=xlrd.open_workbook('test.xlsx')
    #获取所有sheet页的名字
    print(wb.sheet_names())
    #按名字查找第二张表单
    # sheet=wb.sheet_by_name('abc2')#根据sheet页的名字获取sheet页
    sheet = wb.sheet_by_index(0)#根据sheet页的索引获取sheet页
    #获取sheet页的行数和列数
    print(sheet.nrows)
    print(sheet.ncols)
    #打印每行信息
    for rownum in range(sheet.nrows):  #循环取每行的数据
        print(sheet.row_values(rownum))#取每行的数据
    #按照索引打印对应单元格内容
    cell_A2=sheet.cell(0,1).value#获取指定单元格的值，第一个值是列，第二个值是行
    print(cell_A2)


# 将excel数据转化成列表: [{},{}]
def excel_list():
    wb = xlrd.open_workbook('test.xlsx')
    sheet = wb.sheet_by_index(0)
    row_num, clo_num = sheet.nrows, sheet.ncols
    result = []
    field = sheet.row_values(0)
    for row in range(1, row_num):
        obj = {}
        data = sheet.row_values(row)
        for i in range(clo_num):
            obj[field[i]] = data[i]
        result.append(obj)
    print(result)


excel_list()