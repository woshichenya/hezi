# -*- coding: UTF-8 -*-

from plus_vdong.all_table_compute.data_compute.wxapp_visit_compute import DbWxappVisitComputer


class DbPlusWxappVisit(object):
    _data = []
    _result = {'uniacid': 0, 'session_cnt': 0, 'visit_pv': 0, 'visit_uv': 0, 'visit_uv_new': 0, 'visit_total': 0,
               'stay_time_uv': 0.00, 'share_uv': 0, 'share_pv': 0, 'visit_depth': 0.00,
               'stay_time_session': 0.00, 'create_date': '0000-00-00'}

    def __init__(self, uniacid, date, key, secret):
        self._result['uniacid'] = uniacid
        self.date = date
        self.key = key
        self.secret = secret

    def set_data(self):

        visit_data, over_view = (DbWxappVisitComputer(self.date, self.key, self.secret)).get_result()
        data = dict(visit_data[0], **over_view[0])
        self._result['create_date'] = self.date.strftime('%Y-%m-%d')

        for key in self._result:
            if data.has_key(key):
                self._result[key] = data[key]

        self._data.append(self._result)

    def get_data(self):
        self.set_data()
        return self._data
