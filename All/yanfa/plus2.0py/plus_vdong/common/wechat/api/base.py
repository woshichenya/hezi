# -*- coding: utf-8 -*-

import datetime

class WechatBaseApi(object):

    def __init__(self,client = None):
        self._client = client
    def _get(self, url, **kwargs):
        if getattr(self, 'API_BASE_URL', None):
            kwargs['api_base_url'] = self.API_BASE_URL
        return self._client.get(url, **kwargs)

    def _post(self, url, **kwargs):
        if getattr(self, 'API_BASE_URL', None):
            kwargs['api_base_url'] = self.API_BASE_URL
        return self._client.post(url, **kwargs)

    @property
    def access_token(self):
        return self._client.access_token

    @property
    def appid(self):
        return self._client.key

    @classmethod
    def _to_date_str(cls, date):
        # if isinstance(date, (datetime.datetime, datetime.date)):
        #     return date.strftime('%Y-%m-%d')
        # else:
        #     raise ValueError('Can not convert %s type to str', type(date))
        return date