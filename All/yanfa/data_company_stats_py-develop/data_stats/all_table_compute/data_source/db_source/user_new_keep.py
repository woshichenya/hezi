# -*- coding: UTF-8 -*-

from data_stats.tableModel.db_base_model import DataUserNewKeep


class DataUserNewKeepSource(object):

    def __init__(self):
        self._table = DataUserNewKeep

    def get_info_someday(self,query_date):
        try:
            return self._table().select().where(self._table.create_date == query_date).get().dicts()
        except Exception as e:
            return None

    def count_new_user_active_someday(self,reg_date,active_date):
        try:
            sql = "select count(*) as num from data_middle_save_user LEFT JOIN data_middle_user on data_middle_save_user.data_user_id = data_middle_user.id where data_middle_save_user.create_date = '%s' and data_middle_user.last_login = '%s'"%(reg_date,active_date)
            res = self._table().raw(sql).get()
            return res.num
        except Exception:
            return None
