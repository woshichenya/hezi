# -*- coding: UTF-8 -*-
from db_insert import DbInsertBase,insert,PlusWechatsMemberAnalysis,PlusWechatsArticleReadChannel,PlusWechatsArticleReadCount
from data_stats.all_table_compute.data_table.plus_wechats_member_analysis import DbPlusWechatsMemberAnalysis
from data_stats.all_table_compute.data_table.plus_wechats_article_read_channel import DbPlusWechatsArticleReadChannel
from data_stats.all_table_compute.data_table.plus_wechats_article_read_count import DbPlusWechatsArticleReadCount


class DbInsertVipcn(DbInsertBase):

    type = 2

    # 插入用户关注表
    def wechats_member_analysis(self):
        data = DbPlusWechatsMemberAnalysis(self.uniacid,self.date,self.key,self.secret).get_data()
        if data:
            insert(PlusWechatsMemberAnalysis, [data])

    # 渠道来源
    def wechats_article_read_channel(self):
        data = DbPlusWechatsArticleReadChannel(self.uniacid, self.date, self.key, self.secret).get_data()
        if data:
            insert(PlusWechatsArticleReadChannel, data)
        pass

    # 阅读统计
    def wechats_article_read_count(self):
        data = DbPlusWechatsArticleReadCount(self.uniacid, self.date, self.key, self.secret).get_data()
        if data:
            # print data
            insert(PlusWechatsArticleReadCount, [data])






