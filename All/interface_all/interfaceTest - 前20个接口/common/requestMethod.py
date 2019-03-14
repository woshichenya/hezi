import requests
import json
import logging
#######################################################
logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#logging.basicConfig(level = logging.DEBUG,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
#######################################################

class requestMethod():

    def getMethod(self,url,datas):
        r = requests.get(url, datas)
        status_code=r.status_code
        myJson=r.json()
        logger.info("这是接口返回的json值——：{}".format(myJson))
        msg = myJson['msg']


        post_dict={}
        post_dict['codeStatus']=status_code
        post_dict['msg'] = msg
        post_dict['json'] = myJson

        return post_dict

#############################################################

    def postMethod_interface1(self,url,datas):
        r = requests.post(url, datas)
        status_code=r.status_code
        myJson=r.json()
        logger.info("这是接口返回的json值——：{}".format(myJson))
        msg = myJson['msg']
        body = myJson['body']
        body_dict = json.loads(body)
        alipay_open_agent_create_response = body_dict['alipay_open_agent_create_response']
        batch_no = alipay_open_agent_create_response['batch_no']

        post_in1_dict={}
        post_in1_dict['codeStatus']=status_code
        post_in1_dict['msg'] = msg
        post_in1_dict['json'] = myJson
        post_in1_dict['batch_no'] = batch_no

        return post_in1_dict

    def postMethod_interface3(self,url,datas):
        r = requests.post(url, datas)
        status_code=r.status_code
        myJson=r.json()
        logger.info("这是接口返回的json值——：{}".format(myJson))
        msg = myJson['msg']

        body = myJson['body']
        body_dict = json.loads(body)
        alipay_open_auth_token_app_response = body_dict['alipay_open_auth_token_app_response']
        tokens = alipay_open_auth_token_app_response['tokens']
        tokens_0 = tokens[0]
        app_auth_token = tokens_0['app_auth_token']

        #appAuthToken = myJson['appAuthToken']

        post_in3_dict={}
        post_in3_dict['codeStatus']=status_code
        post_in3_dict['msg'] = msg
        post_in3_dict['json'] = myJson
        post_in3_dict['appAuthToken'] = app_auth_token

        return post_in3_dict

    def postMethod_interface5(self,url,datas):
        r = requests.post(url, datas)
        status_code=r.status_code
        myJson=r.json()
        logger.info("这是接口返回的json值——：{}".format(myJson))
        msg = myJson['msg']

        body = myJson['body']
        body_dict = json.loads(body)
        alipay_open_auth_token_app_response = body_dict['alipay_open_auth_token_app_response']
        tokens = alipay_open_auth_token_app_response['tokens']
        tokens_0 = tokens[0]
        app_auth_token = tokens_0['app_auth_token']

        post_in5_dict={}
        post_in5_dict['codeStatus']=status_code
        post_in5_dict['msg'] = msg
        post_in5_dict['json'] = myJson
        post_in5_dict['accessToken'] = app_auth_token

        return post_in5_dict


    def postMethod(self,url,datas):
        r = requests.post(url, datas)
        status_code=r.status_code
        myJson=r.json()
        logger.info("这是接口返回的json值——：{}".format(myJson))
        msg = myJson['msg']


        post_dict={}
        post_dict['codeStatus']=status_code
        post_dict['msg'] = msg
        post_dict['json'] = myJson


        return post_dict



