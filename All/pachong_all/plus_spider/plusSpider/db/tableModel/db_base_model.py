# -*- coding: UTF-8 -*-
# *******************************************************************************************
# **  文件名称：db_base_model.py
# **  功能描述：表模型
# **
# **  创 建 者: tangyongchun
# **  创建日期: 2018-11-13
# ********************************************************************************************


from peewee import *
from plusSpider.common.static import public_args as p_a

database = MySQLDatabase(p_a.database,
                         **{'host': p_a.host, 'user': p_a.user, 'use_unicode': True, 'passwd': p_a.password,
                            'charset': 'utf8', 'port': p_a.port})


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = database


class ImsPlusHotArticle(BaseModel):
    agree_sum = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_time = IntegerField()
    gzh_biz = CharField()
    gzh_title = CharField()
    hot_word_title = CharField()
    read_sum = IntegerField(constraints=[SQL("DEFAULT 0")])
    title = CharField()
    url = CharField()
    article_class = CharField()

    class Meta:
        table_name = 'ims_plus_hot_article'


class ImsPlusHotGzh(BaseModel):
    biz = CharField()
    auth = CharField()
    average_nottop_agree = CharField(constraints=[SQL("DEFAULT '0'")])
    average_nottop_read = CharField(constraints=[SQL("DEFAULT '0'")])
    average_send_article = FloatField(constraints=[SQL("DEFAULT 0.0")])
    average_top_agree = CharField(constraints=[SQL("DEFAULT '0'")])
    average_top_read = CharField(constraints=[SQL("DEFAULT '0'")])
    create_time = IntegerField(constraints=[SQL("DEFAULT 0")])
    logo = CharField()
    max_read_sum = CharField(constraints=[SQL("DEFAULT '0'")])
    new_send_time = IntegerField()
    qr_code_url = CharField()
    remark = TextField(constraints=[SQL("DEFAULT ''")])
    send_article_sum = IntegerField(constraints=[SQL("DEFAULT 0")])
    title = CharField(index=True)
    uin_hao = CharField()
    vdong_index = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'ims_plus_hot_gzh'


class ImsPlusHotGzhInfo(BaseModel):
    agree_sum = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_time = IntegerField(index=True)
    gzh_title = CharField()
    gzh_biz = CharField(index=True)
    ranking = IntegerField(constraints=[SQL("DEFAULT 0")])
    read_sum = IntegerField(constraints=[SQL("DEFAULT 0")])
    send_read_sum = IntegerField(constraints=[SQL("DEFAULT 0")])
    top_agree_sum = IntegerField(constraints=[SQL("DEFAULT 0")])
    top_read_sum = IntegerField(constraints=[SQL("DEFAULT 0")])
    vdong_index = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'ims_plus_hot_gzh_info'
        indexes = (
            (('gzh', 'create_time'), False),
        )


class ImsPlusHotWord(BaseModel):
    create_time = IntegerField(constraints=[SQL("DEFAULT 0")])
    gzh_article_read = TextField()
    gzh_class = TextField()
    hot_rank = IntegerField(constraints=[SQL("DEFAULT 0")])
    title = CharField(index=True)
    vdong_index = FloatField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'ims_plus_hot_word'


class ImsPlusHotWordInfo(BaseModel):
    agree_sum = IntegerField(constraints=[SQL("DEFAULT 0")])
    article_sum = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_date = IntegerField()
    hot_word_title = CharField()
    read_sum = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'ims_plus_hot_word_info'
