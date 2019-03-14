# -*- coding: UTF-8 -*-

from plus_vdong.tableModel.off_db_base_model import PlusMiddleShopMember

class PlusMiddleShopMemberSource(object):

    def __init__(self):
        self._table = PlusMiddleShopMember

    def select_query_date_openid(self,uniacid,query_date):
        openid = []
        data = self._table().select(self._table.openid).where((self._table.uniacid == uniacid) & (self._table.create_date == query_date))
        for item in data:
            openid.append(item.openid)
        return openid