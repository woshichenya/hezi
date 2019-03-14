import xlrd
import xlwt
from xlutils.copy import copy
from shutil import copyfile
import os
import time
import logging
##############################
logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#logging.basicConfig(level = logging.DEBUG,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
##############################
class excelHandle():         #定义一个处理excel的类，参数filePath定义excel文件的路径，
    def __init__(self,path):
        self.path=path

    # 定义一个拷贝excel的函数，复制一个excel文件，文件名带字符串timeNow
    def excelCopy(self):
        now=str(int(time.time()*1000))   ###这是13位的时间戳
        #now = time.strftime('%Y-%m-%d_%H_%M_%S_')  #######取一下当前的时间戳
        logger.debug("now is:{}".format(now))
        #source='{}.xlsx'.format(self.path)
        source = '{}.xls'.format(self.path)
        #target='{0}_{1}.xlsx'.format(self.path,now)
        target = '{0}_{1}.xls'.format(self.path, now)

        try:
            copyfile(source,target)
        except IOError as e:
            print("unable to copy file .%s" %e)
        return now

    # 定义个将excel转换成directory的函数，把excel文件的第一行（标题）与第n行对应的值转换成字典
    ##path定义文件路径；sheetNum定义的是excel的第几个工作表，如0是第一个工作表；norTest定义测试第几行数据，如2即可测试第2行数据
    def excelToDir(self,path, sheetnum, row):  ###path是文件路径，sheetnum是第几个工作表，rows是表格的第几行
        dir_case = path
        data = xlrd.open_workbook(dir_case)
        table = data.sheets()[sheetnum]
        nol = table.ncols
        dict = {}
        for j in range(nol):
            title = table.cell_value(0, j)
            value = table.cell_value(row, j)  ####row是第几行            value值全部转成str类型
            if (type(value)==float):
                value=int(value)
            value = str(value)                     ##############################################

            dict[title] = value
        return dict

    #####定义一个函数，获取某一个sheet有几个测试case
    def getCaseNum(self,path, sheetnum):            ###path是文件路径，sheetnum是第几个工作表####返回值即为有几个/行测试用例
        dir_case = path
        data = xlrd.open_workbook(dir_case)
        table = data.sheets()[sheetnum]
        nor = table.nrows
        for i in range(1, nor):
            title = table.cell_value(0, 1)
            value = table.cell_value(i, 1)
            if (value == ''):
                break
        caseNum = (i - 1)
        return caseNum

    ####定义一个函数，获取某一个sheet中的sign在第几列
    def signLocation(self,path, sheetnum):         ###path是文件路径，sheetnum是第几个工作表####返回值即为sign在第几列
        dir_case = path
        data = xlrd.open_workbook(dir_case)
        table = data.sheets()[sheetnum]
        nor = table.nrows
        nol = table.ncols
        for i in range(0, nor):
            for j in range(nol):
                if (table.cell_value(i, j) == 'sign'):
                    #print(i)
                    #print(j)
                    num=int(j+1)
                    #print("type of num is:{}".format(type(num)))
                    return num

        ####定义一个函数，获取某一个sheet中的sign在第几列

    def appAuthToken_Location(self, path, sheetnum):  ###path是文件路径，sheetnum是第几个工作表####返回值即为sign在第几列
        dir_case = path
        data = xlrd.open_workbook(dir_case)
        table = data.sheets()[sheetnum]
        nor = table.nrows
        nol = table.ncols
        for i in range(0, nor):
            for j in range(nol):
                if (table.cell_value(i, j) == 'appAuthToken'):
                    # print(i)
                    # print(j)
                    num = int(j + 1)
                    # print("type of num is:{}".format(type(num)))
                    return num

    #####定义一个函数，除了case name, method, sign, code, msg列，其他列留下来成为一个字典
    def simpleDict(self,oldDict):
        try:
            del oldDict['case id']
            del oldDict['method']
            del oldDict['sign']
            del oldDict['status_code']
            del oldDict['msg']
            simpleDict=oldDict
            return simpleDict
        except IOError as e:
            print("unable to simplify dict .%s" % e)

    def simpleDict_sign(self,oldDict):
        try:
            del oldDict['case id']
            del oldDict['method']
            del oldDict['status_code']
            del oldDict['msg']
            
            simpleDict=oldDict
            return simpleDict
        except IOError as e:
            print("unable to simplify dict .%s" % e)


    def excelAddData(self,filename,sheetnum,cor,col,value):

        #打开excel
        rb = xlrd.open_workbook(filename,formatting_info=True)
        #rb = xlrd.open_workbook(filename)
        #复制excel
        wb=copy(rb)
        #从复制的excel得到第几个sheet
        sheet=wb.get_sheet(sheetnum)
        #print(type(sheet))
        sheet.write(cor,col,value)
        os.remove(filename)
        #now = str(int(time.time() * 1000))
        #filename2 = '{0}_{1}.xlsx'.format(self.path, now)
        filename2 = 'test000000.xlsx'
        wb.save(filename2)
        copyfile(filename2, filename)   ####拷贝一份到原来的文件名
        os.remove(filename2)           #把新文件删除掉














