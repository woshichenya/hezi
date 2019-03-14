# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PlusspiderItem(scrapy.Item):
    """ 文章信息 """
    title = scrapy.Field()  # 文章标题
    url = scrapy.Field()  # 文章地址
    gzh_biz = scrapy.Field()  # 微信账号
    gzh_title = scrapy.Field()  # 公众号名称
    read_sum = scrapy.Field()  # 阅读数
    agree_sum = scrapy.Field()  # 点赞数
    hot_word_title = scrapy.Field()  # 热词表title字段
    article_class = scrapy.Field()  # 文章类别
    create_time = scrapy.Field()  # 当前0点时间戳


class PlusspiderlineItem(scrapy.Item):
    """ 热词图表信息 """
    hot_word_title = scrapy.Field()  # 热词表 title字段
    read_sum = scrapy.Field()  # 每天的阅读数
    agree_sum = scrapy.Field()  # 点赞数
    article_sum = scrapy.Field()  # 文章数
    create_date = scrapy.Field()  # 每天的0点日期时间戳


class PlusspiderPieItem(scrapy.Item):
    """ 热词图表信息 """
    title = scrapy.Field()  # 热词
    gzh_class = scrapy.Field()  # 公众号分类统计 json格式
    gzh_article_read = scrapy.Field()  # 公众号阅读统计 json格式
    create_time = scrapy.Field()  # 创建时间


class PlusspiderPieUpdateItem(scrapy.Item):
    """ 更新热词表中的热点排名字段 """
    title = scrapy.Field()  # 热词
    hot_rank = scrapy.Field()  # 热点排名


class PlusspiderGzhItem(scrapy.Item):
    """ 公众号信息 """
    biz = scrapy.Field()  # 抓取文章中的biz
    uin_hao = scrapy.Field()  # 微信号唯一字符串
    logo = scrapy.Field()  # 微信号唯一字符串
    title = scrapy.Field()  # 公众号名称
    auth = scrapy.Field()  # 认证公司
    qr_code_url = scrapy.Field()  # 二维码地址
    new_send_time = scrapy.Field()  # 最后发文时间
    create_time = scrapy.Field()  # 创建时间


class PlusspiderGzhUpdateItem(scrapy.Item):
    """ 公众号基本信息 """
    remark = scrapy.Field()  # 简介
    send_article_sum = scrapy.Field()  # 最近30天发送文章数量
    average_send_article = scrapy.Field()  # 最近30天平均发送文章篇数
    average_top_read = scrapy.Field()  # 头条平均阅读
    average_nottop_read = scrapy.Field()  # 非头条平均阅读
    average_top_agree = scrapy.Field()  # 头条平均点赞数
    # average_nottop_agree = scrapy.Field()  # 非头条平均点赞数
    max_read_sum = scrapy.Field()  # 最高阅读量
    uin_hao = scrapy.Field()  # 微信号


class PlusspiderGzhInfoItem(scrapy.Item):
    """ 公众号信息 """
    gzh_title = scrapy.Field()  # 公众号名称
    gzh_biz = scrapy.Field()  # 抓取文章中的biz
    read_sum = scrapy.Field()  # 总阅读量
    top_read_sum = scrapy.Field()  # 头条阅读量
    agree_sum = scrapy.Field()  # 总点赞数
    top_agree_sum = scrapy.Field()  # 头条点赞数
    send_read_sum = scrapy.Field()  # 发送文章篇数
    ranking = scrapy.Field()  # 总排名
    create_time = scrapy.Field()  # 创建时间


class PlusspiderGzhInfoUpdateItem(scrapy.Item):
    """ 公众号信息 """
    gzh_biz = scrapy.Field()  # 抓取文章中的biz
    ranking = scrapy.Field()  # 总排名
    create_time = scrapy.Field()  # 创建时间
