# -*- coding: utf-8 -*-

import requests
import json
from data_stats.utils.redis_util import redis_db


class Wechat(object):

    _http = requests.session()
    _timeout = 1
    API_BASE_URL = ''

    def __init__(self,key,secret,access_token=None, timeout=None):
        self.key = key
        self.secret = secret
        if timeout:
            self._timeout = timeout
        if access_token:
            self.access_token = access_token
        else:
            self.get_access_token()
        pass

    def get(self, url, **kwargs):
        return self._request(
            method='get',
            url_or_endpoint=url,
            **kwargs
        )

    def post(self, url, **kwargs):
        return self._request(
            method='post',
            url_or_endpoint=url,
            **kwargs
        )

    def _request(self, method, url_or_endpoint, **kwargs):

        if not hasattr(self,'access_token'):
            return False

        if not url_or_endpoint.startswith(('http://', 'https://')):
            api_base_url = kwargs.pop('api_base_url')
            url = '{base}{endpoint}'.format(
                base=api_base_url,
                endpoint=url_or_endpoint
            )
        else:
            url = url_or_endpoint

        if 'params' not in kwargs:
            kwargs['params'] = {}

        if isinstance(kwargs['params'], dict) and \
                'access_token' not in kwargs['params']:
            kwargs['params']['access_token'] = self.access_token

        if isinstance(kwargs.get('data', ''), dict):
            body = json.dumps(kwargs['data'], ensure_ascii=False)
            body = body.encode('utf-8')
            kwargs['data'] = body

        kwargs['timeout'] = kwargs.get('timeout', self._timeout)
        result_processor = kwargs.pop('result_processor', None)
        res = self._http.request(
            method=method,
            url=url,
            **kwargs
        )
        try:
            res.raise_for_status()
        except requests.RequestException as reqe:
            raise Exception('微信接口请求失败 url:%s'%url)

        res_dict = json.loads(res.content.decode('utf-8', 'ignore'), strict=False)
        if res_dict.has_key('errcode') and res_dict['errcode'] is not 0:
            raise Exception('微信接口请求失败 返回内容:%s'%res.content)

        return res_dict if not result_processor else result_processor(res_dict)


    def get_access_token(self):

        if not self.key or not self.secret:
            return False

        if hasattr(self,'access_token'):
            return self.access_token

        access_token = redis_db.get('wechat_access_token'+self.key)

        if access_token :
            self.access_token = access_token
        else:
            url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid='+self.key+'&secret='+self.secret
            res = self._http.get(url)
            try:
                res.raise_for_status()
            except requests.RequestException as reqe:
                return False
            res_dict = json.loads(res.content.decode('utf-8', 'ignore'), strict=False)
            if not res_dict or 'errcode' in res_dict:
                raise RuntimeError( '获取access_token接口请求错误 appid:{0} 错误码:{1} 错误内容:{2}'.format(self.key, res_dict['errcode'], res_dict['errmsg'].encode("utf-8")))
                return False
            self.access_token = res_dict['access_token']
            redis_db.setex('wechat_access_token'+self.key,res_dict['access_token'],res_dict['expires_in'])

        return self.access_token














