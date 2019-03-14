# -*- coding: UTF-8 -*-

from data_stats.tableModel.db_base_model import DataWeichenModuleStats


class DataWeichenModuleStatsSource(object):

    def __init__(self):
        self._table = DataWeichenModuleStats

    def get_module_info_someday(self,query_date,module_name,weichen_version,type):
        '''某天的数据'''
        try:
            return self._table().select().where((self._table.create_date==query_date) & (self._table.module_name==module_name) & (self._table.weichen_version==weichen_version) & (self._table.type==type)).get()
        except Exception:
            return None