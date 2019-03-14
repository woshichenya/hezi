# -*- coding: UTF-8 -*-

from data_stats.tableModel.db_base_model import DataWeichenVersionStats


class DataWeichenVersionStatsSource(object):

    def __init__(self):
        self._table = DataWeichenVersionStats

    def get_info_someday(self,query_date,weichen_version,groupid):
        '''某天的数据'''
        try:
            return self._table().select().where((self._table.create_date == query_date) & (self._table.weichen_version == weichen_version) & (self._table.group == groupid)).get().dicts()
        except Exception:
            return None

