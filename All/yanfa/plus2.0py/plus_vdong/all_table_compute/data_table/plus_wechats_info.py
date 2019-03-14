# -*- coding: UTF-8 -*-
from plus_vdong.common.static import public_args as p_a
from plus_vdong.all_table_compute.data_compute.wechats_info_compute import DbWechatsInfoCompute
class DbPlusWechatsInfo(object):
    def __init__(self):
        self._update_data = []
    def col_rank(self,users,create_date):
        try:
            self._update_data = DbWechatsInfoCompute(users,create_date).get_rank()
        except Exception,f:
            p_a.logger.getLogger().error('error %s' % str(f))
        return self._update_data
