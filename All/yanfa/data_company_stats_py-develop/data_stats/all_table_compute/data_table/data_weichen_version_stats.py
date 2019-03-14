# -*- coding: UTF-8 -*-

from data_stats.all_table_compute.data_compute.data_weichen_version_stats import DataWeichenVersionStatsCompute
from data_stats.all_table_compute.data_source.db_source.weichen_version import DataWeichenVersionSource

class DataWeichenVersionStats(object):
    _data = []
    def __init__(self,query_date):
        self.query_date = query_date

    def set_data(self):
        version_list = DataWeichenVersionSource().select_version_list(0)
        for item in version_list:
            compute = DataWeichenVersionStatsCompute(self.query_date,item.weichen_version,item.group)
            field = {
                'total_user' : compute.total_user(),
                'group_id' : item.group,
                'weichen_version' : item.weichen_version,
                'version_name' : item.group_name
            }
            diff_user = field['total_user'] - compute.last_user()
            field['new_user'] = diff_user if diff_user>1 else 0
            self._data.append(field)

    def get_data(self):
        self.set_data()
        return self._data
