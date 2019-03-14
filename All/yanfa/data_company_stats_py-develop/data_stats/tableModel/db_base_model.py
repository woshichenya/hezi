# -*- coding: UTF-8 -*-

import sys
sys.path.append("..")
from peewee import *
from data_stats.common.static import public_args as p_g

# 连接数据库
database = MySQLDatabase(p_g.database, **{'charset': 'utf8', 'use_unicode': True, 'host': p_g.host, 'user': p_g.user, 'password': p_g.passwd})


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = database

class DataMiddleExpireUser(BaseModel):
    create_date = DateField(constraints=[SQL("DEFAULT 0000-00-00")])
    from_ = CharField(column_name='from', constraints=[SQL("DEFAULT ''")])
    user = IntegerField(column_name='user_id', constraints=[SQL("DEFAULT 0")])
    weichen_version = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'data_middle_expire_user'
        indexes = (
            (('user', 'weichen_version', 'from_'), True),
        )

class DataMiddleGood(BaseModel):
    good_name = CharField()
    goodid = CharField(constraints=[SQL("DEFAULT ''")])
    module_name = CharField(constraints=[SQL("DEFAULT ''")])
    uniacid = CharField(constraints=[SQL("DEFAULT ''")])
    weichen_version = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'data_middle_good'

class DataMiddleOrder(BaseModel):
    create_date = DateField(constraints=[SQL("DEFAULT 0000-00-00")])
    module_name = CharField(constraints=[SQL("DEFAULT ''")])
    orderid = CharField(constraints=[SQL("DEFAULT ''")])
    sale_price = DecimalField(constraints=[SQL("DEFAULT 0.00")])
    status = IntegerField(constraints=[SQL("DEFAULT 1")])
    uniacid = CharField(constraints=[SQL("DEFAULT ''")])
    weichen_version = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'data_middle_order'

class DataMiddleSaveUser(BaseModel):
    create_date = DateField(constraints=[SQL("DEFAULT 0000-00-00")])
    data_user = IntegerField(column_name='data_user_id', constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'data_middle_save_user'

class DataMiddleUser(BaseModel):
    account = CharField(constraints=[SQL("DEFAULT ''")])
    end_date = DateField(constraints=[SQL("DEFAULT 0000-00-00")])
    from_ = CharField(column_name='from', constraints=[SQL("DEFAULT ''")])
    group = CharField(column_name='group_id', constraints=[SQL("DEFAULT '0'")])
    last_login = DateField(constraints=[SQL("DEFAULT 0000-00-00")])
    mobile = CharField(constraints=[SQL("DEFAULT ''")])
    province = CharField(constraints=[SQL("DEFAULT ''")])
    reg_date = DateField(constraints=[SQL("DEFAULT 0000-00-00")])
    start_date = DateField(constraints=[SQL("DEFAULT 0000-00-00")])
    user = CharField(column_name='user_id', constraints=[SQL("DEFAULT ''")])
    weichen_version = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'data_middle_user'
        indexes = (
            (('user', 'from_', 'weichen_version'), True),
        )

class DataSourceWxappVersion(BaseModel):
    modules = TextField()
    uniacid = CharField(constraints=[SQL("DEFAULT ''")])
    weichen_version = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'data_source_wxapp_version'
        indexes = (
            (('uniacid', 'weichen_version'), True),
        )

class DataUserNewKeep(BaseModel):
    create_date = DateField(constraints=[SQL("DEFAULT 0000-00-00")])
    new_user = IntegerField(constraints=[SQL("DEFAULT 0")])
    next_save_user = IntegerField(null=True)
    seventh_save_user = IntegerField(null=True)
    third_save_user = IntegerField(null=True)
    thirtieth_save_user = IntegerField(null=True)

    class Meta:
        table_name = 'data_user_new_keep'

class DataUserProvince(BaseModel):
    province = CharField(constraints=[SQL("DEFAULT ''")])
    user_count = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'data_user_province'

class DataUserStats(BaseModel):
    active_user = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_date = DateField(constraints=[SQL("DEFAULT 0000-00-00")])
    plus_user = IntegerField(constraints=[SQL("DEFAULT 0")])
    total_user = IntegerField(constraints=[SQL("DEFAULT 0")])
    weichen_keep_user = IntegerField(constraints=[SQL("DEFAULT 0")])
    weichen_lose_user = IntegerField(constraints=[SQL("DEFAULT 0")])
    weichen_pay_user = IntegerField(constraints=[SQL("DEFAULT 0")])
    weichen_user = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'data_user_stats'

class DataWeichenAppModule(BaseModel):
    module_name = CharField(constraints=[SQL("DEFAULT ''")])
    uniacid = CharField(constraints=[SQL("DEFAULT ''")])
    weichen_version = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'data_weichen_app_module'
        indexes = (
            (('module_name', 'uniacid', 'weichen_version'), True),
        )

class DataWeichenModule(BaseModel):
    app_support = IntegerField(constraints=[SQL("DEFAULT 2")])
    description = TextField()
    module_name = CharField(constraints=[SQL("DEFAULT ''")])
    module_title = CharField(constraints=[SQL("DEFAULT ''")])
    type = CharField(constraints=[SQL("DEFAULT ''")])
    type_name = CharField(constraints=[SQL("DEFAULT ''")])
    version = CharField(constraints=[SQL("DEFAULT ''")])
    weichen_version = CharField(constraints=[SQL("DEFAULT ''")])
    wxapp_support = IntegerField(constraints=[SQL("DEFAULT 2")])

    class Meta:
        table_name = 'data_weichen_module'
        indexes = (
            (('module_name', 'weichen_version'), True),
        )

class DataWeichenModuleStats(BaseModel):
    create_date = DateField(constraints=[SQL("DEFAULT 0000-00-00")])
    module_name = CharField(constraints=[SQL("DEFAULT ''")])
    module_title = CharField(constraints=[SQL("DEFAULT ''")])
    new_user = IntegerField(constraints=[SQL("DEFAULT 0")])
    total_user = IntegerField(constraints=[SQL("DEFAULT 0")])
    type = IntegerField(constraints=[SQL("DEFAULT 1")])
    weichen_version = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'data_weichen_module_stats'
        indexes = (
            (('module_name', 'weichen_version', 'create_date', 'type'), True),
        )

class DataWeichenShopAppModule(BaseModel):
    create_date = DateField(constraints=[SQL("DEFAULT 0000-00-00")])
    module_name = CharField(constraints=[SQL("DEFAULT ''")])
    module_title = CharField(constraints=[SQL("DEFAULT ''")])
    new_refund = IntegerField(constraints=[SQL("DEFAULT 0")])
    new_success = IntegerField(constraints=[SQL("DEFAULT 0")])
    refund_num = IntegerField(constraints=[SQL("DEFAULT 0")])
    success_num = IntegerField(constraints=[SQL("DEFAULT 0")])
    type_name = CharField(constraints=[SQL("DEFAULT ''")])
    weichen_version = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'data_weichen_shop_app_module'

class DataWeichenTotalStats(BaseModel):
    app_goods_num = IntegerField(constraints=[SQL("DEFAULT 0")])
    app_module_num = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_date = DateField(constraints=[SQL("DEFAULT 0000-00-00")])
    wxapp_goods_num = IntegerField(constraints=[SQL("DEFAULT 0")])
    wxapp_module_num = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'data_weichen_total_stats'

class DataWeichenUserStats(BaseModel):
    create_date = DateField(constraints=[SQL("DEFAULT 0000-00-00")])
    keep_user = IntegerField(constraints=[SQL("DEFAULT 0")])
    lose_user = IntegerField(constraints=[SQL("DEFAULT 0")])
    new_keep_user = IntegerField(constraints=[SQL("DEFAULT 0")])
    new_lose_user = IntegerField(constraints=[SQL("DEFAULT 0")])
    new_pay_user = IntegerField(constraints=[SQL("DEFAULT 0")])
    new_try_user = IntegerField(constraints=[SQL("DEFAULT 0")])
    pay_user = IntegerField(constraints=[SQL("DEFAULT 0")])
    try_user = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'data_weichen_user_stats'

class DataWeichenVersion(BaseModel):
    group = IntegerField(column_name='group_id', constraints=[SQL("DEFAULT 0")])
    group_name = CharField(constraints=[SQL("DEFAULT ''")])
    is_free = IntegerField(constraints=[SQL("DEFAULT 0")])
    weichen_version = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'data_weichen_version'
        primary_key = False

class DataWeichenVersionStats(BaseModel):
    create_date = DateField(constraints=[SQL("DEFAULT 0000-00-00")])
    group = IntegerField(column_name='group_id', constraints=[SQL("DEFAULT 0")])
    new_user = IntegerField(constraints=[SQL("DEFAULT 0")])
    total_user = IntegerField(constraints=[SQL("DEFAULT 0")])
    version_name = CharField(constraints=[SQL("DEFAULT ''")])
    weichen_version = CharField(constraints=[SQL("DEFAULT '4.0'")])

    class Meta:
        table_name = 'data_weichen_version_stats'

class DataWeichenWxappModule(BaseModel):
    module_name = CharField(constraints=[SQL("DEFAULT ''")])
    uniacid = CharField(constraints=[SQL("DEFAULT ''")])
    weichen_version = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'data_weichen_wxapp_module'
        indexes = (
            (('module_name', 'uniacid', 'weichen_version'), True),
        )

class DataWeichenWxappRefundOrder(BaseModel):
    create_date = DateField(constraints=[SQL("DEFAULT 0000-00-00")])
    module_name = CharField(constraints=[SQL("DEFAULT ''")])
    num = IntegerField(constraints=[SQL("DEFAULT 0")])
    price = DecimalField(constraints=[SQL("DEFAULT 0.00")])
    shop_name = CharField(constraints=[SQL("DEFAULT ''")])
    type_name = CharField(constraints=[SQL("DEFAULT ''")])
    weichen_version = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'data_weichen_wxapp_refund_order'

class DataWeichenWxappSuccessOrder(BaseModel):
    create_date = DateField(constraints=[SQL("DEFAULT 0000-00-00")])
    module_name = CharField(constraints=[SQL("DEFAULT ''")])
    num = IntegerField(constraints=[SQL("DEFAULT 0")])
    price = DecimalField(constraints=[SQL("DEFAULT 0.00")])
    shop_name = CharField(constraints=[SQL("DEFAULT ''")])
    type_name = CharField(constraints=[SQL("DEFAULT ''")])
    weichen_version = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'data_weichen_wxapp_success_order'


