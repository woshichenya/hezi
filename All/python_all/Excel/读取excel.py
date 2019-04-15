import xlrd
excel_list=[]
excel=xlrd.open_workbook(filename="D:\linshi\涉及鲜橙收入和金额收入接口.xlsx")
print(excel)
sheets = excel.sheets()  # 获取工作表list。
'''
print(sheets)
sheet = sheets[0]  # 通过索引顺序获取。
sheet = excel.sheet_by_index(0)  # 通过索引顺序获取。
sheet = excel.sheet_by_name(u'Sheet1')  # 通过名称获取。
'''
'''
这里默认取的第一个sheel表
'''
sheet=sheets[0]
'''
读取行列
'''
nrows = sheet.nrows
ncols = sheet.ncols
# print("行：%s\n列：%s"%(ncols,nrows))
'''
将每一行的前五列都读取出来
'''
for hang in range(0,ncols):
    xx=[]
    for lie in range(0,4):
        t = sheet.cell_value(hang, lie)
        if t == "":
            t=sheet.cell_value(1, 1)
        # excel_list[hang,lie]=t
        xx.append(t)
        # print("行：%s列：%s---内容：%s"%(hang,lie,t))
    excel_list.append(xx)

print(excel_list)


