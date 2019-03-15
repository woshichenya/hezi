# -*- coding: UTF-8 -*-

import sys
sys.path.append("..")
from peewee import *
from plus_vdong.common.static import public_args as p_g

# 连接数据库
database = MySQLDatabase(p_g.off_database, **{'charset': 'utf8', 'use_unicode': True, 'host': p_g.off_host, 'user': p_g.off_user, 'password': p_g.off_passwd})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class PlusMiddleShopCategory(BaseModel):
    cateid = CharField()
    name = CharField()
    uniacid = CharField()

    class Meta:
        table_name = 'plus_middle_shop_category'

class PlusMiddleShopGoods(BaseModel):
    create_date = DateField(index=True)
    deleted = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    goodsid = CharField()
    id = IntegerField()
    pcate = IntegerField(constraints=[SQL("DEFAULT 0")])
    price = FloatField(constraints=[SQL("DEFAULT 0")])
    thumb = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    title = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    uniacid = CharField(index=True)

    class Meta:
        table_name = 'plus_middle_shop_goods'
        indexes = (
            (('id', 'pcate'), True),
        )
        primary_key = CompositeKey('id', 'pcate')

class PlusMiddleShopMember(BaseModel):
    city = CharField(constraints=[SQL("DEFAULT ''")])
    create_date = DateField(index=True)
    openid = CharField(unique=True)
    province = CharField(constraints=[SQL("DEFAULT ''")])
    uid = CharField()
    uniacid = CharField(index=True)

    class Meta:
        table_name = 'plus_middle_shop_member'

class PlusMiddleShopOrder(BaseModel):
    create_date = DateField(index=True)
    hour = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_pay = IntegerField(constraints=[SQL("DEFAULT 0")])
    openid = CharField(index=True, null=True)
    orderid = IntegerField()
    pay_date = CharField()
    pay_price = FloatField(constraints=[SQL("DEFAULT 0")])
    paytype = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    status = IntegerField()
    type = IntegerField(constraints=[SQL("DEFAULT 0")])
    uniacid = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    visit_way = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'plus_middle_shop_order'

class PlusMiddleShopOrderGoods(BaseModel):
    create_date = DateField()
    goodsid = CharField()
    is_pay = IntegerField(constraints=[SQL("DEFAULT 0")])
    openid = CharField(null=True)
    orderid = IntegerField(null=True)
    pay_date = CharField(constraints=[SQL("DEFAULT ''")])
    pay_price = FloatField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    total = IntegerField(constraints=[SQL("DEFAULT 0")])
    type = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    uniacid = CharField()
    visit_way = IntegerField()

    class Meta:
        table_name = 'plus_middle_shop_order_goods'

class PlusSourceShopCategory(BaseModel):
    advimg = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    advurl = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    description = CharField(null=True)
    displayorder = IntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True)
    enabled = IntegerField(constraints=[SQL("DEFAULT 1")], index=True, null=True)
    ishome = IntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True)
    isrecommand = IntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True)
    level = IntegerField(null=True)
    name = CharField(null=True)
    parentid = IntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True)
    thumb = CharField(null=True)
    uniacid = IntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True)

    class Meta:
        table_name = 'plus_source_shop_category'

class PlusSourceShopGoods(BaseModel):
    allcates = TextField(null=True)
    artid = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    autoreceive = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    bargain = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    beforehours = IntegerField(constraints=[SQL("DEFAULT 0")])
    buyagain = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    buyagain_commission = TextField(null=True)
    buyagain_condition = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    buyagain_islong = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    buyagain_price = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    buyagain_sale = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    buycontent = TextField(null=True)
    buygroups = TextField(null=True)
    buylevels = TextField(null=True)
    buyshow = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    cannotrefund = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    cardid = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    cash = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    cashier = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    catch = CharField(column_name='catch_id', constraints=[SQL("DEFAULT ''")], null=True)
    catch_source = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    catch_url = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    cates = TextField(null=True)
    catesinit3 = TextField(null=True)
    ccate = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    ccates = TextField(null=True)
    checked = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    city = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    commission = TextField(null=True)
    commission1_pay = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    commission1_rate = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    commission2_pay = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    commission2_rate = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    commission3_pay = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    commission3_rate = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    commission_thumb = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    content = TextField(null=True)
    costprice = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    createtime = IntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True)
    credit = CharField(null=True)
    deduct = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    deduct2 = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    deleted = IntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True)
    description = CharField(null=True)
    detail_btntext1 = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    detail_btntext2 = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    detail_btnurl1 = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    detail_btnurl2 = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    detail_logo = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    detail_shopname = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    detail_totaltitle = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    discounts = TextField(null=True)
    dispatch = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    dispatchid = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    dispatchprice = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    dispatchtype = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    displayorder = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    diyfields = TextField(null=True)
    diyformid = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    diyformtype = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    diymode = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    diypage = IntegerField(null=True)
    diysave = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    diysaveid = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    dowpayment = DecimalField(constraints=[SQL("DEFAULT 0.00")])
    edareas = TextField(null=True)
    edareas_code = TextField()
    edmoney = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    ednum = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    emailstatus = IntegerField(constraints=[SQL("DEFAULT 0")])
    endtime = IntegerField(constraints=[SQL("DEFAULT 0")])
    exchange_postage = DecimalField(constraints=[SQL("DEFAULT 0.00")])
    exchange_stock = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    followtip = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    followurl = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    goodssn = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    groupstype = IntegerField(constraints=[SQL("DEFAULT 0")])
    hascommission = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    hasoption = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    hidecommission = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    intervalfloor = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    intervalprice = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    invoice = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    iscomment = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    isdiscount = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    isdiscount_discounts = TextField(null=True)
    isdiscount_time = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    isdiscount_title = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    isendtime = IntegerField(constraints=[SQL("DEFAULT 0")])
    isforceverifystore = IntegerField(constraints=[SQL("DEFAULT 0")])
    isfullback = IntegerField(constraints=[SQL("DEFAULT 0")])
    ishot = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    islive = IntegerField(constraints=[SQL("DEFAULT 0")])
    isnew = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    isnodiscount = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    ispresell = IntegerField(constraints=[SQL("DEFAULT 0")])
    isrecommand = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    issendfree = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    isstatustime = IntegerField(constraints=[SQL("DEFAULT 0")])
    isstoreprice = IntegerField(constraints=[SQL("DEFAULT 0")])
    istime = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    isverify = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    keywords = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    labelname = TextField(null=True)
    liveprice = DecimalField(constraints=[SQL("DEFAULT 0.00")])
    manydeduct = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    marketprice = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    maxbuy = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    maxliveprice = DecimalField(constraints=[SQL("DEFAULT 0.00")])
    maxprice = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    merchdisplayorder = IntegerField(constraints=[SQL("DEFAULT 0")])
    merchid = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    merchsale = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    minbuy = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    minliveprice = DecimalField(constraints=[SQL("DEFAULT 0.00")])
    minprice = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    minpriceupdated = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    money = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    needfollow = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    newgoods = IntegerField(constraints=[SQL("DEFAULT 0")])
    nocommission = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    nosearch = IntegerField(constraints=[SQL("DEFAULT 0")])
    noticeopenid = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    noticetype = TextField(null=True)
    officthumb = CharField(null=True)
    opencard = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    originalprice = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    pcate = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    pcates = TextField(null=True)
    presellend = IntegerField(constraints=[SQL("DEFAULT 0")])
    presellover = IntegerField(constraints=[SQL("DEFAULT 0")])
    presellovertime = IntegerField()
    presellprice = DecimalField(constraints=[SQL("DEFAULT 0.00")])
    presellsendstatrttime = IntegerField(constraints=[SQL("DEFAULT 0")])
    presellsendtime = IntegerField(constraints=[SQL("DEFAULT 0")])
    presellsendtype = IntegerField(constraints=[SQL("DEFAULT 0")])
    presellstart = IntegerField(constraints=[SQL("DEFAULT 0")])
    preselltimeend = IntegerField(constraints=[SQL("DEFAULT 0")])
    preselltimestart = IntegerField(constraints=[SQL("DEFAULT 0")])
    productprice = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    productsn = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    province = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    quality = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    repair = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    sales = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    salesreal = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    saleupdate = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    saleupdate30424 = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    saleupdate32484 = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    saleupdate33219 = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    saleupdate35843 = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    saleupdate36586 = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    saleupdate37975 = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    saleupdate40170 = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    saleupdate42392 = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    saleupdate51117 = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    saleupdate53481 = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    score = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    seven = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    share_icon = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    share_title = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    sharebtn = IntegerField(constraints=[SQL("DEFAULT 0")])
    shopid = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    shorttitle = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    showgroups = TextField(null=True)
    showlevels = TextField(null=True)
    showsales = IntegerField(constraints=[SQL("DEFAULT 1")])
    showtotal = IntegerField(constraints=[SQL("DEFAULT 0")])
    showtotaladd = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    spec = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    statustimeend = IntegerField(constraints=[SQL("DEFAULT 0")])
    statustimestart = IntegerField(constraints=[SQL("DEFAULT 0")])
    storeids = TextField(null=True)
    subtitle = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    taobaoid = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    taobaourl = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    taotaoid = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    tcate = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    tcates = TextField(null=True)
    tempid = IntegerField(constraints=[SQL("DEFAULT 0")])
    threen = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    thumb = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    thumb_first = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    thumb_url = TextField(null=True)
    timeend = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    timestart = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    title = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    total = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    totalcnf = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    type = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    uniacid = IntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True)
    unit = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    unite_total = IntegerField(constraints=[SQL("DEFAULT 0")])
    updatetime = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    usermaxbuy = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    usetime = IntegerField(constraints=[SQL("DEFAULT 0")])
    verifygoodsdays = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    verifygoodslimitdate = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    verifygoodslimittype = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    verifygoodsnum = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    verifygoodstype = IntegerField(constraints=[SQL("DEFAULT 0")])
    verifytype = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    video = CharField(constraints=[SQL("DEFAULT ''")])
    viewcount = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    virtual = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    virtualsend = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    virtualsendcontent = TextField(null=True)
    weight = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    zq = CharField(column_name='zq_id', constraints=[SQL("DEFAULT ''")], index=True)
    zq_source = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'plus_source_shop_goods'

class PlusSourceShopMember(BaseModel):
    aagentareas = TextField(null=True)
    aagentblack = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    aagentcitys = TextField(null=True)
    aagentlevel = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    aagentnotupgrade = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    aagentprovinces = TextField(null=True)
    aagentstatus = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    aagenttime = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    aagenttype = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    agentblack = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    agentid = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    agentlevel = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    agentnotupgrade = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    agentselectgoods = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    agenttime = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    area = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    authorblack = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    authorid = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    authorlevel = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    authornotupgrade = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    authorstatus = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    authortime = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    avatar = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    avatar_wechat = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    birthday = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    birthmonth = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    birthyear = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    carrier_mobile = CharField(constraints=[SQL("DEFAULT '0'")], null=True)
    childtime = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    city = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    clickcount = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    comefrom = CharField(null=True)
    commission = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    commission_pay = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    commission_total = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    content = TextField(null=True)
    createtime = IntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True)
    credit1 = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    credit2 = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    datavalue = CharField(constraints=[SQL("DEFAULT ''")])
    diyaagentdata = TextField(null=True)
    diyaagentfields = TextField(null=True)
    diyaagentid = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    diyauthordata = TextField(null=True)
    diyauthorfields = TextField(null=True)
    diyauthorid = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    diycommissiondata = TextField(null=True)
    diycommissiondataid = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    diycommissionfields = TextField(null=True)
    diycommissionid = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    diyglobonusdata = TextField(null=True)
    diyglobonusfields = TextField(null=True)
    diyglobonusid = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    diyheadsdata = TextField(null=True)
    diyheadsfields = TextField(null=True)
    diyheadsid = IntegerField(constraints=[SQL("DEFAULT 0")])
    diymaxcredit = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    diymemberdata = TextField(null=True)
    diymemberdataid = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    diymemberfields = TextField(null=True)
    diymemberid = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    endtime2 = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    fixagentid = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    gender = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    groupid = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    hasnewcoupon = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    headsid = IntegerField(constraints=[SQL("DEFAULT 0")])
    headsstatus = IntegerField(constraints=[SQL("DEFAULT 0")])
    headstime = IntegerField(constraints=[SQL("DEFAULT 0")])
    idnumber = CharField(null=True)
    inviter = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    isaagent = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    isagent = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    isauthor = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    isblack = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    isheads = IntegerField(constraints=[SQL("DEFAULT 0")])
    ispartner = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    level = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    maxcredit = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    membercardactive = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    membercardcode = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    membercardid = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    membershipnumber = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    mobile = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    mobileuser = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    mobileverify = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    nickname = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    nickname_wechat = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    noticeset = TextField(null=True)
    openid = CharField(constraints=[SQL("DEFAULT ''")], index=True, null=True)
    openid_qq = CharField(null=True)
    openid_wa = CharField(null=True)
    openid_wx = CharField(null=True)
    partnerblack = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    partnerlevel = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    partnernotupgrade = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    partnerstatus = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    partnertime = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    province = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    pwd = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    realname = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    salt = CharField(null=True)
    status = IntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True)
    uid = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    uniacid = IntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True)
    unionid = CharField(null=True)
    updateaddress = IntegerField(constraints=[SQL("DEFAULT 0")])
    username = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    weixin = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    wxcardupdatetime = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)

    class Meta:
        table_name = 'plus_source_shop_member'

class PlusSourceShopOrder(BaseModel):
    address = TextField(null=True)
    address_send = TextField(null=True)
    addressid = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    agentid = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    apppay = IntegerField(constraints=[SQL("DEFAULT 0")])
    authorid = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    betweenprice = DecimalField(constraints=[SQL("DEFAULT 0.00")])
    borrowopenid = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    buyagainprice = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    cancelpaytime = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    canceltime = IntegerField(null=True)
    carrier = TextField(null=True)
    cash = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    cashtime = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    ces = IntegerField(null=True)
    changedispatchprice = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    changeprice = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    city_express_state = IntegerField(null=True)
    closereason = TextField(null=True)
    commissionmoney = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    contype = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    coupongoodprice = DecimalField(constraints=[SQL("DEFAULT 1.00")], null=True)
    couponid = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    couponmerchid = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    couponprice = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    createtime = IntegerField(index=True, null=True)
    creditadd = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    cycelbuy_periodic = CharField(null=True)
    cycelbuy_predict_time = IntegerField(null=True)
    deductcredit = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    deductcredit2 = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    deductenough = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    deductprice = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    deleted = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    discountprice = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    dispatchid = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    dispatchkey = CharField(constraints=[SQL("DEFAULT ''")])
    dispatchprice = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    dispatchtype = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    dividend = TextField(null=True)
    dividend_applytime = IntegerField(constraints=[SQL("DEFAULT 0")])
    dividend_checktime = IntegerField(constraints=[SQL("DEFAULT 0")])
    dividend_content = TextField(null=True)
    dividend_deletetime = IntegerField(constraints=[SQL("DEFAULT 0")])
    dividend_invalidtime = IntegerField(constraints=[SQL("DEFAULT 0")])
    dividend_paytime = IntegerField(constraints=[SQL("DEFAULT 0")])
    dividend_status = IntegerField(constraints=[SQL("DEFAULT 0")])
    diyformdata = TextField(null=True)
    diyformfields = TextField(null=True)
    diyformid = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    dowpayment = DecimalField(constraints=[SQL("DEFAULT 0.00")])
    express = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    expresscom = CharField(constraints=[SQL("DEFAULT ''")])
    expresssn = CharField(constraints=[SQL("DEFAULT ''")])
    fetchtime = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    finishtime = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    goodsprice = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    grprice = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    headsid = IntegerField(constraints=[SQL("DEFAULT 0")])
    invoice_img = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    invoicename = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    is_cashier = IntegerField(null=True)
    isabonus = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    isauthor = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    isborrow = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    iscomment = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    iscycelbuy = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    isdiscountprice = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    isglobonus = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    ismerch = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    ismr = IntegerField(constraints=[SQL("DEFAULT 0")])
    isnewstore = IntegerField(constraints=[SQL("DEFAULT 0")])
    ispackage = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    isparent = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    isshare = IntegerField(constraints=[SQL("DEFAULT 0")])
    istrade = IntegerField(constraints=[SQL("DEFAULT 0")])
    isverify = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    isvirtual = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    isvirtualsend = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    iswxappcreate = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    liveid = IntegerField(null=True)
    lotterydiscountprice = DecimalField(constraints=[SQL("DEFAULT 0.00")])
    merchapply = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    merchdeductenough = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    merchid = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    merchisdiscountprice = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    merchshow = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    officcode = CharField(constraints=[SQL("DEFAULT ''")])
    olddispatchprice = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    oldprice = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    openid = CharField(constraints=[SQL("DEFAULT ''")], index=True, null=True)
    ordersn = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    ordersn2 = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    ordersn_trade = CharField(null=True)
    packageid = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    parentid = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    paytime = IntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True)
    paytype = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    price = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    print_template = TextField(null=True)
    printstate = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    printstate2 = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    quickid = IntegerField(constraints=[SQL("DEFAULT 0")])
    random_code = CharField(null=True)
    refundid = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    refundstate = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    refundtime = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    remark = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    remarkclose = TextField(null=True)
    remarksaler = TextField(null=True)
    remarksend = TextField(null=True)
    seckilldiscountprice = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    sendtime = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    sendtype = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True)
    storeid = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    sysdeleted = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    taskdiscountprice = DecimalField(constraints=[SQL("DEFAULT 0.00")])
    tradepaytime = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    tradepaytype = IntegerField(null=True)
    tradestatus = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    transid = CharField(constraints=[SQL("DEFAULT '0'")], null=True)
    uniacid = IntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True)
    userdeleted = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    verified = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    verifycode = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    verifycodes = TextField(null=True)
    verifyendtime = IntegerField(constraints=[SQL("DEFAULT 0")])
    verifyinfo = TextField(null=True)
    verifyopenid = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    verifystoreid = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    verifytime = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    verifytype = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    virtual = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    virtual_info = TextField(null=True)
    virtual_str = TextField(null=True)
    virtualsend_info = TextField(null=True)
    willcancelmessage = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    wxapp_prepay = CharField(column_name='wxapp_prepay_id', null=True)
    wxcardid = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    wxcode = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    wxid = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)

    class Meta:
        table_name = 'plus_source_shop_order'

class PlusSourceShopOrderGoods(BaseModel):
    applytime1 = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    applytime2 = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    applytime3 = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    canbuyagain = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    changeprice = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    checktime1 = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    checktime2 = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    checktime3 = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    commission1 = TextField(null=True)
    commission2 = TextField(null=True)
    commission3 = TextField(null=True)
    commissions = TextField(null=True)
    content1 = TextField(null=True)
    content2 = TextField(null=True)
    content3 = TextField(null=True)
    createtime = IntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True)
    deletetime1 = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    deletetime2 = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    deletetime3 = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    diyformdata = TextField(null=True)
    diyformdataid = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    diyformfields = TextField(null=True)
    diyformid = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    dowpayment = DecimalField(constraints=[SQL("DEFAULT 0.00")])
    esheetprintnum = IntegerField(constraints=[SQL("DEFAULT 0")])
    express = CharField()
    expresscom = CharField()
    expresssn = CharField()
    finishtime = IntegerField()
    goodsid = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    goodssn = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    invalidtime1 = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    invalidtime2 = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    invalidtime3 = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    is_make = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    isdiscountprice = DecimalField(constraints=[SQL("DEFAULT 0.00")])
    merchid = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    merchsale = IntegerField(constraints=[SQL("DEFAULT 0")])
    nocommission = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    oldprice = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    openid = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    optime = CharField()
    optionid = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    optionname = TextField(null=True)
    ordercode = CharField()
    orderid = IntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True)
    parentorderid = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    paytime1 = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    paytime2 = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    paytime3 = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    peopleid = IntegerField(constraints=[SQL("DEFAULT 0")])
    price = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    printstate = IntegerField(constraints=[SQL("DEFAULT 0")])
    printstate2 = IntegerField(constraints=[SQL("DEFAULT 0")])
    productsn = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    prohibitrefund = IntegerField(constraints=[SQL("DEFAULT 0")])
    realprice = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    refundtime = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    remarksend = TextField()
    rstate = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    seckill = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    seckill_roomid = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    seckill_taskid = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    seckill_timeid = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    sendtime = IntegerField()
    sendtype = IntegerField(constraints=[SQL("DEFAULT 0")])
    status1 = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    status2 = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    status3 = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    storeid = CharField()
    tdate_time = IntegerField(constraints=[SQL("DEFAULT 0")])
    total = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    trade_time = IntegerField(constraints=[SQL("DEFAULT 0")])
    uniacid = IntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True)

    class Meta:
        table_name = 'plus_source_shop_order_goods'
