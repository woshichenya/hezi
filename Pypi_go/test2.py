from baibaoxiang import sys_powel
import os
# import time
# # aa=os.system("netstat -nat|grep 80|wc -l")
# # print(aa)
# for i in range (100):
#     time.sleep(0.5)
#     k=sys_powel.powel_go().print_cpu()
#
# from baibaoxiang import excel
# x=[1,2,3,4,5,6]
# t=excel.InputExcel()
# t.input_excel(x)
# t.end("D:\\linshi\\","hhhhhhhhhhhhh")


# from baibaoxiang import excel
# s=excel.InputExcel()
# k=[1,2]
# s.input_excel_zidingyi(100,200,k)
# s.end("d:\\linshi\\","随便的名字")



# import xlrd
# from xlutils.copy import copy        #导入copy模块
# rb = xlrd.open_workbook('d:\linshi\\20190419095725随便的名字运行结果.xls','wb')    #打开weng.xls文件/
# wb = copy(rb)                          #利用xlutils.copy下的copy函数复制
# ws = wb.get_sheet(0)                   #获取表单0
# ws.write(0, 0, 'changed!')             #改变（0,0）的值
# ws.write(8,0,label = '好的')           #增加（8,0）的值
# wb.save('d:\linshi\\20190419095725随便的名字运行结果.xls')                    #保存文件



from selenium import webdriver
go=webdriver.Firefox()
go.get("https://www.baidu.com")

from baibaoxiang import baibaoxiang
url="https://www.baidu.com"
go=baibaoxiang.geturl(url)
