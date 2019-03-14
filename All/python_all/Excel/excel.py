import xlsxwriter
import time

class go:
    def __init__(self):
        print("调用excel方法")
    def input_ex(self,hang_0,lie_0,neirong,file_name,file_lujing):
        if file_lujing =="":
            tt=time.strftime("%Y%m%d%H%M",time.localtime())
            test_book = xlsxwriter.Workbook(tt+file_name+".xlsx")
            worksheet = test_book.add_worksheet('what')
            # 定义初始值是h,l
            worksheet.write(hang_0, lie_0, neirong)
            test_book.close()

        if file_lujing!="juedui":
            tt = time.strftime("%Y%m%d%H%M", time.localtime())
            test_book = xlsxwriter.Workbook(file_lujing+tt+file_name+".xlsx")
            worksheet = test_book.add_worksheet('what')
            #定义初始值是h,l
            worksheet.write(hang_0, lie_0, neirong)
            test_book.close()



g=go()
g.input_ex(0,0,100,"","D:\linshi\\test22\\")
g.input_ex(0,1,100,"","D:\linshi\\test22\\")

