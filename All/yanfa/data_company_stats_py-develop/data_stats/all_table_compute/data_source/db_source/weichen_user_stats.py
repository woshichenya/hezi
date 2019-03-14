# -*- coding: UTF-8 -*-

from data_stats.tableModel.db_base_model import DataWeichenUserStats


class DataWeichenUserStatsSource(object):

    def __init__(self):
        self._table = DataWeichenUserStats

    def get_info_someday(self,query_date):
        '''某天的数据'''
        try:
            return self._table().select().where(self._table.create_date == query_date).get().dicts()
        except Exception:
            return None

