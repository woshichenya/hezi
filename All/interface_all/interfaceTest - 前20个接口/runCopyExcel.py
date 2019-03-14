import common.excelHandle
import common.md5Handle
import common.configHandle
import time

import logging
#######################################################
logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#logging.basicConfig(level = logging.DEBUG,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
#######################################################
###用到的变量
testConfig=common.configHandle.getConfig()
myPrivateKey=testConfig.get_excelname()       ####私钥，定义到全局ini文件中
excelName=testConfig.get_excelname()          ####原始excel名称，不带扩展名，定义到全局ini文件中
my_sheet_num=int(testConfig.get_sheetnum())       ####有几个工作表（目前有几个工作表即有几个接口），如我目前有2个sheet，可以定义到全局ini文件中


#######################################################
##第1步，给excel文件做个备份，新拷贝一个excel文件
#excelName='apipayOpen'            ###原来的excel名称，不带扩展名，可以定义到全局ini文件中
path='testCaseExcel/{}'.format(excelName)
myExcel=common.excelHandle.excelHandle(path)
nowTime=myExcel.excelCopy()    ###返回拷贝文件当时的时间
#newExcelName='{0}_{1}.xlsx'.format(excelName,nowTime)
newExcelName='{0}_{1}.xls'.format(excelName,nowTime)
####获取拷贝后的文件名称
logger.debug("new excel name is:{}".format(newExcelName))
newExcel='{0}_{1}'.format(excelName,nowTime)                  ######################################################################
testConfig.set_newexcelname(newExcel)

newPath='testCaseExcel/{}'.format(newExcelName)
logger.debug("new path is:{}".format(newPath))









