#打开excel
import xlrd
import xlwt

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


#excel_list()

def excel_write(excel_name='data.xls', sheet_name='sheet1', data=[]):
    if len(data) == 0:
        print('Please input data')
        return
    wb = xlwt.Workbook(encoding='utf-8')  # 设置编码格式
    my_sheet = wb.add_sheet(sheet_name)
    """向excel写入内容，内容自定义"""
    style = xlwt.XFStyle()  # 初始化样式
    font = xlwt.Font()  # 为样式创建字体
    font.name = 'Times New Roman'
    # font.bold = True                                  # 黑体
    # font.underline = True                             # 下划线
    # font.italic = True                                # 斜体字
    style.font = font  # 设定样式
    data1 = data[0]
    fields = list(data1.keys())
    for i in range(len(fields)):
        my_sheet.write(0, i, fields[i])# 参数对应 行, 列, 值
    for i in range(len(data)):
        for j in range(len(fields)):
            my_sheet.write(i + 1, j, data[i][fields[j]])

    wb.save( excel_name)


excel_write(data=[{'field1':1,'field2':2},{'field1':2,'field2':3}])

