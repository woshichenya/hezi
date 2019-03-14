# -*- coding: UTF-8 -*-

from data_stats.tableModel.db_base_model import DataMiddleExpireUser


class DataMiddleExpireUserSource(object):

    def __init__(self):
        self._table = DataMiddleExpireUser

    def count_keep_user(self):
        try:
            sql = 'SELECT ' \
            'count(*) as num ' \
            'FROM data_middle_expire_user ' \
            'LEFT JOIN data_middle_user ON data_middle_expire_user.`from` = data_middle_user.`from` ' \
            'AND data_middle_expire_user.weichen_version = data_middle_user.weichen_version and data_middle_user.user_id = data_middle_user.user_id ' \
            'where data_middle_user.end_date >  data_middle_expire_user.create_date'
            res = self._table().raw(sql).get()
            return res.num
        except Exception as e:
            return 0
