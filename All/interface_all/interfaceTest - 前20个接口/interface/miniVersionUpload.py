import common.excelHandle
import common.md5Handle
import common.configHandle
import common.requestMethod

import logging
#######################################################
logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#logging.basicConfig(level = logging.DEBUG,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
#######################################################

#######################################################
class miniVersionUpload():


    def miniVersionUpload_case1_request(self,newPath,myPrivateKey):
        sheet=10

        testConfig = common.configHandle.getConfig()
        url = testConfig.get_url()

        interface11= testConfig.get_interface("INTERFACE11", "interface11")
        url11='{0}{1}'.format(url,interface11)

        logger.info("第11个接口的url是:{}".format(url11))


        ################################
        myExcelNew = common.excelHandle.excelHandle(newPath)
        myMd5 = common.md5Handle.md5Handle()
        dict = myExcelNew.excelToDir(newPath,sheet,1)      ######第一行，即第一个case
        simp_dict = myExcelNew.simpleDict(dict)
        md5 = myMd5.signature(simp_dict, myPrivateKey)
        sign_nol = int(myExcelNew.signLocation(newPath,sheet))-1
        myExcelNew.excelAddData(newPath,sheet, 1, sign_nol, md5)

        dict01 = myExcelNew.excelToDir(newPath, sheet, 1)     #####再次读取excel表格中的内容
        simp_dict01 = myExcelNew.simpleDict_sign(dict01)       ####此处即为入参
        logger.info("第11个接口的入参是:{}".format(simp_dict01))

        myPost=common.requestMethod.requestMethod()
        myRequest_dict=myPost.getMethod(url11,simp_dict01)


        return myRequest_dict





'''
mytest=miniCreate()
path_12='G:\\autoTestInterface\\interfaceTest\\testCaseExcel\\apipayOpen_1545372736234.xls'
key_12='MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCjvvZNwrkr2Rt6mA/Zrkgo01zWBJN62VGtU1GGmsQNOzDZHWBwo/3Za/5b4uHpI6tbC96UctoFxrHVH0jqiKFHFD5v38zYVNkSDm65raNz466C3Ao0WNZN/GWavZybRq4C47Csb1/KkTigTrim2sItSda4C2tv3K28bZW/7Eb5/N5BJMN7d7IE2NCwgjF/4KDd2CRqIuNJ+vHAt1JX2pWnrRPWBHmL9GWxaQgbl2J+aH+6kQ1nQ0gri2v/FzoXGUu88N7+iG/FOOc1udrvckAQzaszb0BUQ9lu/75NczNZKcnJBq4L6llZqR4o6+VJK3lyH3gPOrvGEqCutxgm1nyjAgMBAAECggEBAJIHZYTnmVffYMAuCESrRrMR/ALpRdUTJeIbIeOW9iyOkvutVSpfNa3Gv6qWZb4TD2g8550f6AuqrUFRiyeN/bZz+VKwFfD/ii6uLFTu44wgiqstLPSOHWCjLMGZQ6a+m8T75b2B/b2bURK14br78JuO9CxiEshJ167pU9k7D/kz+pq4aAJZou26yYOm10YAN+9cd594aJ8Nfl0ceBi+ZfFnwPM3eUntma9euXf8cmYPxkhvBsR8rQ4/ELg79d3rMt2HhPQJKGt2Hkb/Q3Di+ppWxQF3PJRcueQqeChzsOIvSemYYkj+FBOJ9OWbuT07JbT3cPwavuRJ2QsTkZbIs/ECgYEAzT7FZePDNixK2o5c5yLu7lSTsOJfd/x/4D0tDX22Vn0gtUouTU8pCWM4nsIaCdsOpabT8UKraUQZGB0NaHT5kIiLfYK+mgQKIJq7PIuk66H8mWECGsK1VNDOSbq1jHCnYJomaOmuvLman4ML2Po5L/eLMeuNL9YxOIBX6k1B1/8CgYEAzD0LSCKwAG9GgfQQuec+dqlzYCBvtv5L7GcixTgXwqqxtmyu83lOXNXmk6HOPsaTOJcZ7ZEkw22QqPubQXMGOhEpJLUCfD+rUi+a4/IDgVl6wgzkGgP+mp6lqsTHpnrCteI9he1UChX8kcPA61boZIMq/mvhf8g2AeJLmxjc+10CgYAmkHbSsDsLwMLH0hwOqfeu/GFLyR0bFGyKm7QNZuON2LD+n1OX3xnc07Hd0qbF100nPvNvz5EZlFwKtdrBF8mUqLNc/+YEVmH4wloQBEUWqTcnMp0Mni0oJJu+KsDWBIzOj+hLqizU9SLieeMN/+Yi5yZWWOYMaPiSnzrloWKPzQKBgHMXVzswKOQl0KK8qYxJLl7qAFVEEhAZ3yj5uZNPl7wgOoLlXfVf/3O7KfM5tCKV/jJem8LPDtt9643+MzA/pFumffvscNkZe+6VWwBmyejjRpUBdKzgYWI6UnsX5rX+6ahbNHY7FieU2j4+BIHZ+J1jeR/kJS+/4AdRwW9GJIkVAoGAe+jCewsfPE1J9CIfK/p6sBYXgo/CYQo31x456S5mhNYcn+b+cIDhiyz4m1oQqqxGxZFdgwb7ZtWzpv5W3AulPd2yxy3Uj4JnUcUAkPBMhlw9vSHeqixQBESPUTxCoY52F1xBF7hlcjOsPv+TYkktdApVw+ceZzWqU99x1wjdV5U='
aaa=mytest.miniCreate_case1_request(path_12,key_12)
print(aaa)
'''














