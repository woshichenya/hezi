# -*- coding: UTF-8 -*-

from db_insert import DbInsertBase, p_a, PlusWxappVisit, insert, PlusWxappMemberKeep, PlusWxappMemberActiveKeep
from data_stats.all_table_compute.data_table.plus_wxapp_member_active_keep import DbPlusWxappMemberActiveKeep
from data_stats.all_table_compute.data_table.plus_wxapp_member_keep import DbPlusWxappMemberKeep
from data_stats.all_table_compute.data_table.data_user_province import DbPlusWxappVisit


class DbInsertApplet(DbInsertBase):
    '''小程序'''
    type = 1

    def insert_wxapp_visit(self):
        '''小程序用户访问数据'''
        try:
            data = DbPlusWxappVisit(self.uniacid, self.date, self.key, self.secret).get_data()
            if data:
                insert(PlusWxappVisit, data)
        except Exception, e:
            p_a.logger.getLogger().error('小程序用户访问数据 异常：%s', e)

    def insert_plus_wxapp_member_keep(self):
        try:
            plus_wxapp_member_keep = DbPlusWxappMemberKeep(self.uniacid, self.date)
            data = plus_wxapp_member_keep.get_data()
            if data:
                insert(PlusWxappMemberKeep, data)
        except Exception, e:
            p_a.logger.getLogger().error('PlusWxappMemberKeep 异常：%s', e)

    def insert_plus_wxapp_member_active_keep(self):
        try:
            plus_wxapp_member_active_keep = DbPlusWxappMemberActiveKeep(self.uniacid, self.date)
            data = plus_wxapp_member_active_keep.get_data()
            if data:
                insert(PlusWxappMemberActiveKeep, data)
        except Exception, e:
            p_a.logger.getLogger().error('PlusWxappMemberActiveKeep 异常：%s', e)


    def insert_wxapp_data(self):
        self.insert_wxapp_visit()
        self.insert_plus_wxapp_member_keep()
        self.insert_plus_wxapp_member_active_keep()


