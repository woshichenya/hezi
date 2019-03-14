# -*- coding: UTF-8 -*-

from data_stats.tableModel.db_base_model import DataMiddleUser


class DataMiddleUserSource(object):

    def __init__(self):
        self._table = DataMiddleUser

    def count_total_user(self):
        '''所有用户数'''
        return self._table().select().count()

    def count_user_for_form(self,from_type):
        '''某个平台的用户数'''
        return self._table().select().where(self._table.from_==from_type).count()

    def count_user_from_reg_date(self,rege_date):
        '''某日注册用户数'''
        return self._table().select().where(self._table.reg_date==rege_date).count()

    def count_user_from_active_date(self,last_login):
        '''某日活跃用户数'''
        return self._table().select().where(self._table.last_login==last_login).count()

    def select_user_from_reg_date(self, rege_date):
        '''某日注册用户列表'''
        return self._table().select().where(self._table.reg_date==rege_date)

    def select_weichen_total_user(self):
        '''所有微尘用户数'''
        return self._table().select().where(self._table.from_=='weichen').dicts()

    def select_user_from_active_date(self,last_login):
        '''某日活跃用户列表'''
        return self._table().select().where(self._table.last_login==last_login)

    def select_user_from_end_date(self,end_date):
        '''某日到期用户列表'''
        return self._table().select().where(self._table.end_date==end_date)

    def count_group_user_with_weichen(self,groupid,weichen_version):
        '''微尘组用户数'''
        return self._table().select().where((self._table.group==groupid) & (self._table.weichen_version==weichen_version)).count()

    def count_weichen_lose_user(self,query_date):
        '''流失'''
        return self._table().select().where((self._table.end_date < query_date) & (self._table.from_=='weichen')).count()

    def select_user_province(self):
        '''省份列表'''
        sql = "select count(id) as num,province from data_middle_user GROUP BY province"
        return self._table().raw(sql).dicts()
