import os
import xlsxwriter
import time


res="D:\\linshi\\test22"
os.makedirs(res)     #简单点就是这个样子，创建一个文件夹
book = xlsxwriter.Workbook(res+'\\107.xlsx')
# 在G盘xxoo文件下创建103的excel


worksheet = book.add_worksheet('s001')
# 103的excel的sheet页名称为s001

'''excel表格的行标和列标是从0开始的'''
for i in range(0,1000000):
    for s in range(0,3):
        if s==0:
            worksheet.write(i, s, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # 第i行第s列赋值当前时间
        if s == 1:
            worksheet.write(i, s, "yonghuming")
        if s == 2:
            worksheet.write(i, s, "mima")
        #worksheet.write('z4', 111)  # A4单元格赋值111
# 写入信息
book.close()
print("共",i+1,"行----共",s+1,"列-------")



