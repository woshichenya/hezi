
import unittest

import interface.agentCreate
import interface.miniCreate
import interface.getAuthToken
import interface.authTokenQuery
import interface.oauth
import interface.userAuth
import interface.userInfoShare
import interface.addMembers
import interface.queryMembers
import interface.deleteMembers
import interface.miniVersionUpload
import interface.miniExperienceCreate
import interface.miniExperienceQuery
import interface.miniBaseInfoQuery       #第14个接口
import interface.miniBaseInfoModify      #第15个接口
import interface.miniGrayCancel      #第16个接口
import interface.miniVersionListQuery   #第17个接口
import interface.miniTemplateUsage    #第18个接口
import interface.miniVersionDetailQuery  #第19个接口
import interface.miniAuditedCancel    #第20个接口

import common.configHandle
import common.excelHandle
import HTMLTestRunner
import time

import logging
#######################################################
logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#logging.basicConfig(level = logging.DEBUG,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
#######################################################
now = time.strftime('%Y-%m-%d_%H_%M_%S_')              #######取一下当前的时间戳

#######################################################
##第2步，对新拷贝的excel文件进行操作——即进行测试用例执行
class interfaceTest(unittest.TestCase):
    #@unittest.skip('调过第1个接口的测试用例')          #调过第1个接口
    def test_agentCreate(self):                          ################执行第1个接口
        testConfig = common.configHandle.getConfig()
        myPrivateKey = testConfig.get_privatekey()
        newPath = testConfig.get_newexcelname()
        #newPath = 'G:\\autoTestInterface\\interfaceTest\\testCaseExcel\\{}.xls'.format(newPath)
        newPath = 'testCaseExcel/{}.xls'.format(newPath)
        mytest = interface.agentCreate.agentCreate()

        ######获取第一个接口的返回值，包括code status，json，msg，batch_no

        agentCreateDict = mytest.agentCreate_case1_request(newPath, myPrivateKey)
        agentCreate_case1_status = agentCreateDict['codeStatus']
        #agentCreate_case1_status = int (agentCreate_case1_status)
        logger.debug("agentCreate interface code status is:{}".format(agentCreate_case1_status))
        self.assertEqual(200, agentCreate_case1_status, '测试第1个接口的返回状态码有问题，不是200')
        agentCreate_case1_json = agentCreateDict['json']
        logger.debug("agentCreate interface json is:{}".format(agentCreate_case1_json))
        agentCreate_case1_msg = agentCreateDict['msg']
        logger.debug("agentCreate interface message is:{}".format(agentCreate_case1_msg))
        #self.assertEqual('Success', agentCreate_case1_msg, '测试第1个接口的返回msg有问题，不是Success')
        self.assertEqual('Success', agentCreate_case1_msg,agentCreate_case1_json)
        #self.assertEqual('Success', agentCreate_case1_msg, agentCreate_case1_json)
        agentCreate_case1_batch_no = agentCreateDict['batch_no']
        logger.debug("agentCreate interface batch_no is:{}".format(agentCreate_case1_batch_no))        ###############取出第1个接口的batch_no给以后的接口使用

        myExcel=common.excelHandle.excelHandle(newPath)
        myExcel.excelAddData(newPath,1,1,2,agentCreate_case1_batch_no)            ######把第一个接口的返回值给到第二个接口的入参，加入到excel表单的sheet1-（1,2）

    #@unittest.skip('调过第2个接口的测试用例')  # 调过第2个接口
    def test_miniCreate(self):                          ################执行第2个接口
        testConfig = common.configHandle.getConfig()
        myPrivateKey = testConfig.get_privatekey()
        newPath = testConfig.get_newexcelname()
        #newPath = 'G:\\autoTestInterface\\interfaceTest\\testCaseExcel\\{}.xls'.format(newPath)
        newPath = 'testCaseExcel/{}.xls'.format(newPath)
        mytest = interface.miniCreate.miniCreate()

        ######获取第2个接口的返回值，包括code status，json，msg，batch_no

        miniCreateDict = mytest.miniCreate_case1_request(newPath, myPrivateKey)
        miniCreate_case1_status = miniCreateDict['codeStatus']
        miniCreate_case1_status = int (miniCreate_case1_status)
        logger.debug("miniCreate interface code status is:{}".format(miniCreate_case1_status))
        self.assertEqual(200, miniCreate_case1_status, '测试第2个接口的返回状态码有问题，不是200')
        miniCreate_case1_json = miniCreateDict['json']
        logger.debug("miniCreate interface json is:{}".format(miniCreate_case1_json))
        miniCreate_case1_msg = miniCreateDict['msg']
        logger.debug("miniCreate interface message is:{}".format(miniCreate_case1_msg))
        #self.assertEqual('Success', miniCreate_case1_msg, '测试第2个接口的返回msg有问题，不是Success')
        self.assertEqual('Success', miniCreate_case1_msg,miniCreate_case1_json)

    #@unittest.skip('调过第3个接口的测试用例')  # 调过第3个接口
    def test_getAuthToken(self):                          ################执行第3个接口
        testConfig = common.configHandle.getConfig()
        myPrivateKey = testConfig.get_privatekey()
        newPath = testConfig.get_newexcelname()
        #newPath = 'G:\\autoTestInterface\\interfaceTest\\testCaseExcel\\{}.xls'.format(newPath)
        newPath = 'testCaseExcel/{}.xls'.format(newPath)
        mytest = interface.getAuthToken.getAuthToken()

        ######获取第3个接口的返回值，包括code status，json，msg

        getAuthTokenDict = mytest.getAuthToken_case1_request(newPath, myPrivateKey)
        getAuthToken_case1_status = getAuthTokenDict['codeStatus']
        #getAuthToken_case1_status = int (getAuthToken_case1_status)
        logger.debug("getAuthToken interface code status is:{}".format(getAuthToken_case1_status))
        self.assertEqual(200, getAuthToken_case1_status, '测试第3个接口的返回状态码有问题，不是200')
        getAuthToken_case1_json = getAuthTokenDict['json']
        logger.debug("getAuthToken interface json is:{}".format(getAuthToken_case1_json))
        getAuthToken_case1_msg = getAuthTokenDict['msg']
        logger.debug("getAuthToken interface message is:{}".format(getAuthToken_case1_msg))
        #self.assertEqual('Success', getAuthToken_case1_msg, '测试第3个接口的返回msg有问题，不是Success')
        self.assertEqual('Success', getAuthToken_case1_msg, getAuthToken_case1_json)

        getAuthToken_case1_appAuthToken = getAuthTokenDict['appAuthToken']
        logger.debug("agentCreate interface appAuthToken is:{}".format(getAuthToken_case1_appAuthToken))  ###############取出第3个接口的appAuthToken给以后的接口使用

        myExcel = common.excelHandle.excelHandle(newPath)
        myExcel.excelAddData(newPath, 3, 1, 2,getAuthToken_case1_appAuthToken)  ######把第3个接口的返回值给到第4个接口的入参，加入到excel表单的sheet3（1,2）
        myExcel.excelAddData(newPath, 7, 1, 4,getAuthToken_case1_appAuthToken)  ######把第3个接口的返回值给到第8个接口的入参，加入到excel表单的sheet7（1,4）
        myExcel.excelAddData(newPath, 8, 1, 3,getAuthToken_case1_appAuthToken)  ######把第3个接口的返回值给到第9个接口的入参，加入到excel表单的sheet8（1,3）
        myExcel.excelAddData(newPath, 9, 1, 4,getAuthToken_case1_appAuthToken)  ######把第3个接口的返回值给到第10个接口的入参，加入到excel表单的sheet9（1,4）
        myExcel.excelAddData(newPath, 10, 1, 5,getAuthToken_case1_appAuthToken)  ######把第3个接口的返回值给到第11个接口的入参，加入到excel表单的sheet10（1,5）
        myExcel.excelAddData(newPath, 11, 1, 3,getAuthToken_case1_appAuthToken)  ######把第3个接口的返回值给到第12个接口的入参，加入到excel表单的sheet11（1,3）
        myExcel.excelAddData(newPath, 12, 1, 3,getAuthToken_case1_appAuthToken)  ######把第3个接口的返回值给到第13个接口的入参，加入到excel表单的sheet12（1,3）
        myExcel.excelAddData(newPath, 13, 1, 2,getAuthToken_case1_appAuthToken)  ######把第3个接口的返回值给到第14个接口的入参，加入到excel表单的sheet13（1,2）
        myExcel.excelAddData(newPath, 14, 1, 5,getAuthToken_case1_appAuthToken)  ######把第3个接口的返回值给到第15个接口的入参，加入到excel表单的sheet14（1,5）
        myExcel.excelAddData(newPath, 15, 1, 3,getAuthToken_case1_appAuthToken)  ######把第3个接口的返回值给到第16个接口的入参，加入到excel表单的sheet15（1,3）
        myExcel.excelAddData(newPath, 16, 1, 2,getAuthToken_case1_appAuthToken)  ######把第3个接口的返回值给到第17个接口的入参，加入到excel表单的sheet16（1,2）
        myExcel.excelAddData(newPath, 17, 1, 6,getAuthToken_case1_appAuthToken)  ######把第3个接口的返回值给到第18个接口的入参，加入到excel表单的sheet17（1,6）
        myExcel.excelAddData(newPath, 18, 1, 3,getAuthToken_case1_appAuthToken)  ######把第3个接口的返回值给到第19个接口的入参，加入到excel表单的sheet18（1,3）
        myExcel.excelAddData(newPath, 19, 1, 3,getAuthToken_case1_appAuthToken)  ######把第3个接口的返回值给到第20个接口的入参，加入到excel表单的sheet19（1,3）


    #@unittest.skip('调过第4个接口的测试用例')  # 调过第4个接口
    def test_authTokenQuery(self):  ################执行第4个接口
        testConfig = common.configHandle.getConfig()
        myPrivateKey = testConfig.get_privatekey()
        newPath = testConfig.get_newexcelname()
        # newPath = 'G:\\autoTestInterface\\interfaceTest\\testCaseExcel\\{}.xls'.format(newPath)
        newPath = 'testCaseExcel/{}.xls'.format(newPath)
        mytest = interface.authTokenQuery.authTokenQuery()

        ######获取第4个接口的返回值，包括code status，json，msg

        authTokenQueryDict = mytest.authTokenQuery_case1_request(newPath, myPrivateKey)
        authTokenQuery_case1_status = authTokenQueryDict['codeStatus']
        # authTokenQuery_case1_status = int (authTokenQuery_case1_status)
        logger.debug("authTokenQuery interface code status is:{}".format(authTokenQuery_case1_status))
        self.assertEqual(200, authTokenQuery_case1_status, '测试第4个接口的返回状态码有问题，不是200')
        authTokenQuery_case1_json = authTokenQueryDict['json']
        logger.debug("authTokenQuery interface json is:{}".format(authTokenQuery_case1_json))
        authTokenQuery_case1_msg = authTokenQueryDict['msg']
        logger.debug("authTokenQuery interface message is:{}".format(authTokenQuery_case1_msg))
        #self.assertEqual('Success', authTokenQuery_case1_msg, '测试第4个接口的返回msg有问题，不是Success')
        self.assertEqual('Success', authTokenQuery_case1_msg,authTokenQuery_case1_json)

    #@unittest.skip('调过第5个接口的测试用例')
    def test_oauth(self):  ################执行第5个接口
        testConfig = common.configHandle.getConfig()
        myPrivateKey = testConfig.get_privatekey()
        newPath = testConfig.get_newexcelname()
        # newPath = 'G:\\autoTestInterface\\interfaceTest\\testCaseExcel\\{}.xls'.format(newPath)
        newPath = 'testCaseExcel/{}.xls'.format(newPath)
        mytest = interface.oauth.oauth()

        ######获取第4个接口的返回值，包括code status，json，msg

        oauthDict = mytest.oauth_case1_request(newPath, myPrivateKey)
        oauth_case1_status = oauthDict['codeStatus']
        # oauth_case1_status = int (oauth_case1_status)
        logger.debug("oauth interface code status is:{}".format(oauth_case1_status))
        self.assertEqual(200, oauth_case1_status, '测试第5个接口的返回状态码有问题，不是200')
        oauth_case1_json = oauthDict['json']
        logger.debug("oauth interface json is:{}".format(oauth_case1_json))
        #oauth_case1_msg = oauthDict['msg']
        #logger.debug("oauth interface message is:{}".format(oauth_case1_msg))
        #self.assertEqual('None', oauth_case1_msg, '测试第5个接口的返回msg有问题，不是null')  ########这个接口比较奇怪，msg是null

        oauth_case1_accessToken = oauthDict['accessToken']
        logger.debug("oauth interface accessToken is:{}".format(oauth_case1_accessToken))  ###############取出第5个接口的accessToken给以后的接口使用

        print(oauth_case1_accessToken)

        myExcel = common.excelHandle.excelHandle(newPath)
        myExcel.excelAddData(newPath, 6, 1, 2,oauth_case1_accessToken)  ######把第5个接口的返回值给到第7个接口的入参，加入到excel表单的sheet6（1,2）


    @unittest.skip('调过第6个接口的测试用例')  # 调过第6个接口（#####################################页面跳转的不需要判断测试结果#########################）
    def test_userAuth(self):  ################执行第6个接口   （页面跳转的不需要判断测试结果）
        testConfig = common.configHandle.getConfig()
        myPrivateKey = testConfig.get_privatekey()
        newPath = testConfig.get_newexcelname()
        # newPath = 'G:\\autoTestInterface\\interfaceTest\\testCaseExcel\\{}.xls'.format(newPath)
        newPath = 'testCaseExcel/{}.xls'.format(newPath)
        mytest = interface.userAuth.userAuth()

        ######获取第6个接口的返回值，包括code status，json，msg

        userAuthDict = mytest.userAuth_case1_request(newPath, myPrivateKey)
        userAuth_case1_status = userAuthDict['codeStatus']
        # userAuth_case1_status = int (userAuth_case1_status)
        logger.debug("userAuth interface code status is:{}".format(userAuth_case1_status))
        #self.assertEqual(200, userAuth_case1_status, '测试第6个接口的返回状态码有问题，不是200')

    #@unittest.skip('调过第7个接口的测试用例')
    def test_userInfoShare(self):  ################执行第7个接口
        testConfig = common.configHandle.getConfig()
        myPrivateKey = testConfig.get_privatekey()
        newPath = testConfig.get_newexcelname()
        # newPath = 'G:\\autoTestInterface\\interfaceTest\\testCaseExcel\\{}.xls'.format(newPath)
        newPath = 'testCaseExcel/{}.xls'.format(newPath)
        mytest = interface.userInfoShare.userInfoShare()

        ######获取第7个接口的返回值，包括code status，json，msg

        userInfoShareDict = mytest.userInfoShare_case1_request(newPath, myPrivateKey)
        userInfoShare_case1_status = userInfoShareDict['codeStatus']
        # userInfoShare_case1_status = int (userInfoShare_case1_status)
        logger.debug("userInfoShare interface code status is:{}".format(userInfoShare_case1_status))
        self.assertEqual(200, userInfoShare_case1_status, '测试第7个接口的返回状态码有问题，不是200')
        userInfoShare_case1_json = userInfoShareDict['json']
        logger.debug("userInfoShare interface json is:{}".format(userInfoShare_case1_json))
        userInfoShare_case1_msg = userInfoShareDict['msg']
        logger.debug("userInfoShare interface message is:{}".format(userInfoShare_case1_msg))
        #self.assertEqual('Success', userInfoShare_case1_msg, '测试第7个接口的返回msg有问题，不是Success')
        self.assertEqual('Success', userInfoShare_case1_msg,userInfoShare_case1_json)

    def test_addMembers(self):  ################执行第8个接口
        testConfig = common.configHandle.getConfig()
        myPrivateKey = testConfig.get_privatekey()
        newPath = testConfig.get_newexcelname()
        # newPath = 'G:\\autoTestInterface\\interfaceTest\\testCaseExcel\\{}.xls'.format(newPath)
        newPath = 'testCaseExcel/{}.xls'.format(newPath)
        mytest = interface.addMembers.addMembers()

        ######获取第8个接口的返回值，包括code status，json，msg

        addMembersDict = mytest.addMembers_case1_request(newPath, myPrivateKey)
        addMembers_case1_status = addMembersDict['codeStatus']
        # addMembers_case1_status = int (addMembers_case1_status)
        logger.debug("addMembers interface code status is:{}".format(addMembers_case1_status))
        self.assertEqual(200, addMembers_case1_status, '测试第8个接口的返回状态码有问题，不是200')
        addMembers_case1_json = addMembersDict['json']
        logger.debug("addMembers interface json is:{}".format(addMembers_case1_json))
        addMembers_case1_msg = addMembersDict['msg']
        logger.debug("addMembers interface message is:{}".format(addMembers_case1_msg))
        #self.assertEqual('Success', addMembers_case1_msg, '测试第8个接口的返回msg有问题，不是Success')
        self.assertEqual('Success', addMembers_case1_msg,addMembers_case1_json)

    def test_queryMembers(self):  ################执行第9个接口
        testConfig = common.configHandle.getConfig()
        myPrivateKey = testConfig.get_privatekey()
        newPath = testConfig.get_newexcelname()
        # newPath = 'G:\\autoTestInterface\\interfaceTest\\testCaseExcel\\{}.xls'.format(newPath)
        newPath = 'testCaseExcel/{}.xls'.format(newPath)
        mytest = interface.queryMembers.queryMembers()

        ######获取第9个接口的返回值，包括code status，json，msg

        queryMembersDict = mytest.queryMembers_case1_request(newPath, myPrivateKey)
        queryMembers_case1_status = queryMembersDict['codeStatus']
        # queryMembers_case1_status = int (queryMembers_case1_status)
        logger.debug("queryMembers interface code status is:{}".format(queryMembers_case1_status))
        self.assertEqual(200, queryMembers_case1_status, '测试第9个接口的返回状态码有问题，不是200')
        queryMembers_case1_json = queryMembersDict['json']
        logger.debug("queryMembers interface json is:{}".format(queryMembers_case1_json))
        queryMembers_case1_msg = queryMembersDict['msg']
        logger.debug("queryMembers interface message is:{}".format(queryMembers_case1_msg))
        #self.assertEqual('Success', queryMembers_case1_msg, '测试第9个接口的返回msg有问题，不是Success')
        self.assertEqual('Success', queryMembers_case1_msg, queryMembers_case1_json)

    def test_deleteMembers(self):  ################执行第10个接口
        testConfig = common.configHandle.getConfig()
        myPrivateKey = testConfig.get_privatekey()
        newPath = testConfig.get_newexcelname()
        # newPath = 'G:\\autoTestInterface\\interfaceTest\\testCaseExcel\\{}.xls'.format(newPath)
        newPath = 'testCaseExcel/{}.xls'.format(newPath)
        mytest = interface.deleteMembers.deleteMembers()

        ######获取第10个接口的返回值，包括code status，json，msg

        deleteMembersDict = mytest.deleteMembers_case1_request(newPath, myPrivateKey)
        deleteMembers_case1_status = deleteMembersDict['codeStatus']
        # deleteMembers_case1_status = int (deleteMembers_case1_status)
        logger.debug("deleteMembers interface code status is:{}".format(deleteMembers_case1_status))
        self.assertEqual(200, deleteMembers_case1_status, '测试第10个接口的返回状态码有问题，不是200')
        deleteMembers_case1_json = deleteMembersDict['json']
        logger.debug("deleteMembers interface json is:{}".format(deleteMembers_case1_json))
        deleteMembers_case1_msg = deleteMembersDict['msg']
        logger.debug("deleteMembers interface message is:{}".format(deleteMembers_case1_msg))
        #self.assertEqual('Success', deleteMembers_case1_msg, '测试第10个接口的返回msg有问题，不是Success')
        self.assertEqual('Success', deleteMembers_case1_msg, deleteMembers_case1_json)

    def test_miniVersionUpload(self):  ################执行第11个接口
        testConfig = common.configHandle.getConfig()
        myPrivateKey = testConfig.get_privatekey()
        newPath = testConfig.get_newexcelname()
        # newPath = 'G:\\autoTestInterface\\interfaceTest\\testCaseExcel\\{}.xls'.format(newPath)
        newPath = 'testCaseExcel/{}.xls'.format(newPath)
        mytest = interface.miniVersionUpload.miniVersionUpload()

        ######获取第11个接口的返回值，包括code status，json，msg

        miniVersionUploadDict = mytest.miniVersionUpload_case1_request(newPath, myPrivateKey)
        miniVersionUpload_case1_status = miniVersionUploadDict['codeStatus']
        # miniVersionUpload_case1_status = int (miniVersionUpload_case1_status)
        logger.debug("miniVersionUpload interface code status is:{}".format(miniVersionUpload_case1_status))
        self.assertEqual(200, miniVersionUpload_case1_status, '测试第11个接口的返回状态码有问题，不是200')
        miniVersionUpload_case1_json = miniVersionUploadDict['json']
        logger.debug("miniVersionUpload interface json is:{}".format(miniVersionUpload_case1_json))
        miniVersionUpload_case1_msg = miniVersionUploadDict['msg']
        logger.debug("miniVersionUpload interface message is:{}".format(miniVersionUpload_case1_msg))
        self.assertEqual('Success', miniVersionUpload_case1_msg, miniVersionUpload_case1_json)

    def test_miniExperienceCreate(self):  ################执行第12个接口
        testConfig = common.configHandle.getConfig()
        myPrivateKey = testConfig.get_privatekey()
        newPath = testConfig.get_newexcelname()
        # newPath = 'G:\\autoTestInterface\\interfaceTest\\testCaseExcel\\{}.xls'.format(newPath)
        newPath = 'testCaseExcel/{}.xls'.format(newPath)
        mytest = interface.miniExperienceCreate.miniExperienceCreate()

        ######获取第12个接口的返回值，包括code status，json，msg

        miniExperienceCreateDict = mytest.miniExperienceCreate_case1_request(newPath, myPrivateKey)
        miniExperienceCreate_case1_status = miniExperienceCreateDict['codeStatus']
        # miniExperienceCreate_case1_status = int (miniExperienceCreate_case1_status)
        logger.debug("miniExperienceCreate interface code status is:{}".format(miniExperienceCreate_case1_status))
        self.assertEqual(200, miniExperienceCreate_case1_status, '测试第12个接口的返回状态码有问题，不是200')
        miniExperienceCreate_case1_json = miniExperienceCreateDict['json']
        logger.debug("miniExperienceCreate interface json is:{}".format(miniExperienceCreate_case1_json))
        miniExperienceCreate_case1_msg = miniExperienceCreateDict['msg']
        logger.debug("miniExperienceCreate interface message is:{}".format(miniExperienceCreate_case1_msg))
        self.assertEqual('Success', miniExperienceCreate_case1_msg, miniExperienceCreate_case1_json)

    def test_miniExperienceQuery(self):  ################执行第13个接口
        testConfig = common.configHandle.getConfig()
        myPrivateKey = testConfig.get_privatekey()
        newPath = testConfig.get_newexcelname()
        # newPath = 'G:\\autoTestInterface\\interfaceTest\\testCaseExcel\\{}.xls'.format(newPath)
        newPath = 'testCaseExcel/{}.xls'.format(newPath)
        mytest = interface.miniExperienceQuery.miniExperienceQuery()

        ######获取第13个接口的返回值，包括code status，json，msg

        miniExperienceQueryDict = mytest.miniExperienceQuery_case1_request(newPath, myPrivateKey)
        miniExperienceQuery_case1_status = miniExperienceQueryDict['codeStatus']
        # miniExperienceQuery_case1_status = int (miniExperienceQuery_case1_status)
        logger.debug("miniExperienceQuery interface code status is:{}".format(miniExperienceQuery_case1_status))
        self.assertEqual(200, miniExperienceQuery_case1_status, '测试第13个接口的返回状态码有问题，不是200')
        miniExperienceQuery_case1_json = miniExperienceQueryDict['json']
        logger.debug("miniExperienceQuery interface json is:{}".format(miniExperienceQuery_case1_json))
        miniExperienceQuery_case1_msg = miniExperienceQueryDict['msg']
        logger.debug("miniExperienceQuery interface message is:{}".format(miniExperienceQuery_case1_msg))
        self.assertEqual('Success', miniExperienceQuery_case1_msg, miniExperienceQuery_case1_json)

    def test_miniBaseInfoQuery(self):  ################执行第14个接口
        testConfig = common.configHandle.getConfig()
        myPrivateKey = testConfig.get_privatekey()
        newPath = testConfig.get_newexcelname()
        # newPath = 'G:\\autoTestInterface\\interfaceTest\\testCaseExcel\\{}.xls'.format(newPath)
        newPath = 'testCaseExcel/{}.xls'.format(newPath)
        mytest = interface.miniBaseInfoQuery.miniBaseInfoQuery()
        ######获取第14个接口的返回值，包括code status，json，msg
        miniBaseInfoQueryDict = mytest.miniBaseInfoQuery_case1_request(newPath, myPrivateKey)
        miniBaseInfoQuery_case1_status = miniBaseInfoQueryDict['codeStatus']
        # miniBaseInfoQuery_case1_status = int (miniBaseInfoQuery_case1_status)
        logger.debug("miniBaseInfoQuery interface code status is:{}".format(miniBaseInfoQuery_case1_status))
        self.assertEqual(200, miniBaseInfoQuery_case1_status, '测试第14个接口的返回状态码有问题，不是200')
        miniBaseInfoQuery_case1_json = miniBaseInfoQueryDict['json']
        logger.debug("miniBaseInfoQuery interface json is:{}".format(miniBaseInfoQuery_case1_json))
        miniBaseInfoQuery_case1_msg = miniBaseInfoQueryDict['msg']
        logger.debug("miniBaseInfoQuery interface message is:{}".format(miniBaseInfoQuery_case1_msg))
        self.assertEqual('Success', miniBaseInfoQuery_case1_msg, miniBaseInfoQuery_case1_json)

    def test_miniBaseInfoModify(self):  ################执行第15个接口
        testConfig = common.configHandle.getConfig()
        myPrivateKey = testConfig.get_privatekey()
        newPath = testConfig.get_newexcelname()
        # newPath = 'G:\\autoTestInterface\\interfaceTest\\testCaseExcel\\{}.xls'.format(newPath)
        newPath = 'testCaseExcel/{}.xls'.format(newPath)
        mytest = interface.miniBaseInfoModify.miniBaseInfoModify()
        ######获取第15个接口的返回值，包括code status，json，msg
        miniBaseInfoModifyDict = mytest.miniBaseInfoModify_case1_request(newPath, myPrivateKey)
        miniBaseInfoModify_case1_status = miniBaseInfoModifyDict['codeStatus']
        # miniBaseInfoModify_case1_status = int (miniBaseInfoModify_case1_status)
        logger.debug("miniBaseInfoModify interface code status is:{}".format(miniBaseInfoModify_case1_status))
        self.assertEqual(200, miniBaseInfoModify_case1_status, '测试第15个接口的返回状态码有问题，不是200')
        miniBaseInfoModify_case1_json = miniBaseInfoModifyDict['json']
        logger.debug("miniBaseInfoModify interface json is:{}".format(miniBaseInfoModify_case1_json))
        miniBaseInfoModify_case1_msg = miniBaseInfoModifyDict['msg']
        logger.debug("miniBaseInfoModify interface message is:{}".format(miniBaseInfoModify_case1_msg))
        self.assertEqual('Success', miniBaseInfoModify_case1_msg, miniBaseInfoModify_case1_json)

    def test_miniGrayCancel(self):  ################执行第16个接口
        testConfig = common.configHandle.getConfig()
        myPrivateKey = testConfig.get_privatekey()
        newPath = testConfig.get_newexcelname()
        # newPath = 'G:\\autoTestInterface\\interfaceTest\\testCaseExcel\\{}.xls'.format(newPath)
        newPath = 'testCaseExcel/{}.xls'.format(newPath)
        mytest = interface.miniGrayCancel.miniGrayCancel()
        ######获取第16个接口的返回值，包括code status，json，msg
        miniGrayCancelDict = mytest.miniGrayCancel_case1_request(newPath, myPrivateKey)
        miniGrayCancel_case1_status = miniGrayCancelDict['codeStatus']
        # miniGrayCancel_case1_status = int (miniGrayCancel_case1_status)
        logger.debug("miniGrayCancel interface code status is:{}".format(miniGrayCancel_case1_status))
        self.assertEqual(200, miniGrayCancel_case1_status, '测试第16个接口的返回状态码有问题，不是200')
        miniGrayCancel_case1_json = miniGrayCancelDict['json']
        logger.debug("miniGrayCancel interface json is:{}".format(miniGrayCancel_case1_json))
        miniGrayCancel_case1_msg = miniGrayCancelDict['msg']
        logger.debug("miniGrayCancel interface message is:{}".format(miniGrayCancel_case1_msg))
        self.assertEqual('Success', miniGrayCancel_case1_msg, miniGrayCancel_case1_json)

    def test_miniVersionListQuery(self):  ################执行第17个接口
        testConfig = common.configHandle.getConfig()
        myPrivateKey = testConfig.get_privatekey()
        newPath = testConfig.get_newexcelname()
        # newPath = 'G:\\autoTestInterface\\interfaceTest\\testCaseExcel\\{}.xls'.format(newPath)
        newPath = 'testCaseExcel/{}.xls'.format(newPath)
        mytest = interface.miniVersionListQuery.miniVersionListQuery()
        ######获取第17个接口的返回值，包括code status，json，msg
        miniVersionListQueryDict = mytest.miniVersionListQuery_case1_request(newPath, myPrivateKey)
        miniVersionListQuery_case1_status = miniVersionListQueryDict['codeStatus']
        # miniVersionListQuery_case1_status = int (miniVersionListQuery_case1_status)
        logger.debug("miniVersionListQuery interface code status is:{}".format(miniVersionListQuery_case1_status))
        self.assertEqual(200, miniVersionListQuery_case1_status, '测试第17个接口的返回状态码有问题，不是200')
        miniVersionListQuery_case1_json = miniVersionListQueryDict['json']
        logger.debug("miniVersionListQuery interface json is:{}".format(miniVersionListQuery_case1_json))
        miniVersionListQuery_case1_msg = miniVersionListQueryDict['msg']
        logger.debug("miniVersionListQuery interface message is:{}".format(miniVersionListQuery_case1_msg))
        self.assertEqual('Success', miniVersionListQuery_case1_msg, miniVersionListQuery_case1_json)

    def test_miniTemplateUsage(self):  ################执行第18个接口
        testConfig = common.configHandle.getConfig()
        myPrivateKey = testConfig.get_privatekey()
        newPath = testConfig.get_newexcelname()
        # newPath = 'G:\\autoTestInterface\\interfaceTest\\testCaseExcel\\{}.xls'.format(newPath)
        newPath = 'testCaseExcel/{}.xls'.format(newPath)
        mytest = interface.miniTemplateUsage.miniTemplateUsage()
        ######获取第18个接口的返回值，包括code status，json，msg
        miniTemplateUsageDict = mytest.miniTemplateUsage_case1_request(newPath, myPrivateKey)
        miniTemplateUsage_case1_status = miniTemplateUsageDict['codeStatus']
        # miniTemplateUsage_case1_status = int (miniTemplateUsage_case1_status)
        logger.debug("miniTemplateUsage interface code status is:{}".format(miniTemplateUsage_case1_status))
        self.assertEqual(200, miniTemplateUsage_case1_status, '测试第18个接口的返回状态码有问题，不是200')
        miniTemplateUsage_case1_json = miniTemplateUsageDict['json']
        logger.debug("miniTemplateUsage interface json is:{}".format(miniTemplateUsage_case1_json))
        miniTemplateUsage_case1_msg = miniTemplateUsageDict['msg']
        logger.debug("miniTemplateUsage interface message is:{}".format(miniTemplateUsage_case1_msg))
        self.assertEqual('Success', miniTemplateUsage_case1_msg, miniTemplateUsage_case1_json)

    def test_miniVersionDetailQuery(self):  ################执行第19个接口
        testConfig = common.configHandle.getConfig()
        myPrivateKey = testConfig.get_privatekey()
        newPath = testConfig.get_newexcelname()
        # newPath = 'G:\\autoTestInterface\\interfaceTest\\testCaseExcel\\{}.xls'.format(newPath)
        newPath = 'testCaseExcel/{}.xls'.format(newPath)
        mytest = interface.miniVersionDetailQuery.miniVersionDetailQuery()
        ######获取第19个接口的返回值，包括code status，json，msg
        miniVersionDetailQueryDict = mytest.miniVersionDetailQuery_case1_request(newPath, myPrivateKey)
        miniVersionDetailQuery_case1_status = miniVersionDetailQueryDict['codeStatus']
        # miniVersionDetailQuery_case1_status = int (miniVersionDetailQuery_case1_status)
        logger.debug("miniVersionDetailQuery interface code status is:{}".format(miniVersionDetailQuery_case1_status))
        self.assertEqual(200, miniVersionDetailQuery_case1_status, '测试第19个接口的返回状态码有问题，不是200')
        miniVersionDetailQuery_case1_json = miniVersionDetailQueryDict['json']
        logger.debug("miniVersionDetailQuery interface json is:{}".format(miniVersionDetailQuery_case1_json))
        miniVersionDetailQuery_case1_msg = miniVersionDetailQueryDict['msg']
        logger.debug("miniVersionDetailQuery interface message is:{}".format(miniVersionDetailQuery_case1_msg))
        self.assertEqual('Success', miniVersionDetailQuery_case1_msg, miniVersionDetailQuery_case1_json)

    def test_miniAuditedCancel(self):  ################执行第20个接口
        testConfig = common.configHandle.getConfig()
        myPrivateKey = testConfig.get_privatekey()
        newPath = testConfig.get_newexcelname()
        # newPath = 'G:\\autoTestInterface\\interfaceTest\\testCaseExcel\\{}.xls'.format(newPath)
        newPath = 'testCaseExcel/{}.xls'.format(newPath)
        mytest = interface.miniAuditedCancel.miniAuditedCancel()
        ######获取第20个接口的返回值，包括code status，json，msg
        miniAuditedCancelDict = mytest.miniAuditedCancel_case1_request(newPath, myPrivateKey)
        miniAuditedCancel_case1_status = miniAuditedCancelDict['codeStatus']
        # miniAuditedCancel_case1_status = int (miniAuditedCancel_case1_status)
        logger.debug("miniAuditedCancel interface code status is:{}".format(miniAuditedCancel_case1_status))
        self.assertEqual(200, miniAuditedCancel_case1_status, '测试第20个接口的返回状态码有问题，不是200')
        miniAuditedCancel_case1_json = miniAuditedCancelDict['json']
        logger.debug("miniAuditedCancel interface json is:{}".format(miniAuditedCancel_case1_json))
        miniAuditedCancel_case1_msg = miniAuditedCancelDict['msg']
        logger.debug("miniAuditedCancel interface message is:{}".format(miniAuditedCancel_case1_msg))
        self.assertEqual('Success', miniAuditedCancel_case1_msg, miniAuditedCancel_case1_json)












#执行测试代码
'''
if __name__=='__main__':
    unittest.main()
'''
if __name__ == '__main__':
    test_suite = unittest.TestSuite()  # 创建一个测试集合

    ##################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    test_suite.addTest(interfaceTest('test_agentCreate'))  ####往suite里面添加测试用例，接口1
    test_suite.addTest(interfaceTest('test_miniCreate'))  ####往suite里面添加测试用例，接口2
    test_suite.addTest(interfaceTest('test_getAuthToken'))  ####往suite里面添加测试用例，接口3
    test_suite.addTest(interfaceTest('test_authTokenQuery'))  ####往suite里面添加测试用例，接口4
    test_suite.addTest(interfaceTest('test_oauth'))  ####往suite里面添加测试用例，接口5
    test_suite.addTest(interfaceTest('test_userAuth'))  ####往suite里面添加测试用例，接口6
    test_suite.addTest(interfaceTest('test_userInfoShare'))  ####往suite里面添加测试用例，接口7
    test_suite.addTest(interfaceTest('test_addMembers'))  ####往suite里面添加测试用例，接口8
    test_suite.addTest(interfaceTest('test_queryMembers'))  ####往suite里面添加测试用例，接口9
    test_suite.addTest(interfaceTest('test_deleteMembers'))  ####往suite里面添加测试用例，接口10
    test_suite.addTest(interfaceTest('test_miniVersionUpload'))  ####往suite里面添加测试用例，接口11
    test_suite.addTest(interfaceTest('test_miniExperienceCreate'))  ####往suite里面添加测试用例，接口12
    test_suite.addTest(interfaceTest('test_miniExperienceQuery'))  ####往suite里面添加测试用例，接口13
    test_suite.addTest(interfaceTest('test_miniBaseInfoQuery'))  ####往suite里面添加测试用例，接口14
    test_suite.addTest(interfaceTest('test_miniBaseInfoModify'))  ####往suite里面添加测试用例，接口15
    test_suite.addTest(interfaceTest('test_miniGrayCancel'))  ####往suite里面添加测试用例，接口16
    test_suite.addTest(interfaceTest('test_miniVersionListQuery'))  ####往suite里面添加测试用例，接口17
    test_suite.addTest(interfaceTest('test_miniTemplateUsage'))  ####往suite里面添加测试用例，接口18
    test_suite.addTest(interfaceTest('test_miniVersionDetailQuery'))  ####往suite里面添加测试用例，接口19
    test_suite.addTest(interfaceTest('test_miniAuditedCancel'))  ####往suite里面添加测试用例，接口20



    # test_suite.addTest(unittest.makeSuite(MyTest))#使用makeSuite方法添加所有的测试方法
    filepath = 'result/report/report_{}.html'.format(now)
    fp = open(filepath, 'wb')  # 打开一个保存结果的html文件
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='支付宝接口测试报告', description='测试情况')
    # 生成执行用例的对象
    runner.run(test_suite)
    # 执行测试套件




'''
if __name__ == '__main__':
    #filepath = 'G:\\autoTestInterface\\interfaceTest\\result\\report\\report_{}.html'.format(now)
    filepath = 'result/report/report_{}.html'.format(now)
    ftp = open(filepath, 'wb')
    suite = unittest.TestSuite()
    ##############@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@############
    suite.addTest(interfaceTest('test_agentCreate'))  ####往suite里面添加测试用例，接口1
    runner = HTMLTestRunner.HTMLTestRunner(stream=ftp, title='支付宝接口测试')
    runner.run(suite)
    unittest.main()
'''























