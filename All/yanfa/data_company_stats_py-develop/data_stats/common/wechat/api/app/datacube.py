# -*- coding: utf-8 -*-

from data_stats.common.wechat.api.base import WechatBaseApi

class DataCube(WechatBaseApi):

    API_BASE_URL = 'https://api.weixin.qq.com/datacube/'


    def get_analysis_daily_retain(self, begin_date, end_date):
        """
        获取用户访问小程序日留存
        详情请参考
        https://developers.weixin.qq.com/miniprogram/dev/api/getAnalysisDailyRetain.html
        :param begin_date: 起始日期
        :param end_date: 结束日期
        :return: 统计数据列表
        """
        res = self._post(
            'getweanalysisappiddailyretaininfo',
            data={
                'begin_date': self._to_date_str(begin_date),
                'end_date': self._to_date_str(end_date)
            },
        )
        return res

    def get_analysis_daily_summary(self, begin_date, end_date):
        """
        获取用户访问小程序数据概况
        详情请参考
        https://developers.weixin.qq.com/miniprogram/dev/api/getAnalysisDailySummary.html
        :param begin_date: 起始日期
        :param end_date: 结束日期
        :return: 统计数据列表
        """
        res = self._post(
            'getweanalysisappiddailysummarytrend',
            data={
                'begin_date': self._to_date_str(begin_date),
                'end_date': self._to_date_str(end_date)
            },
            result_processor = lambda x: x['list']
        )
        return res

    def get_analysis_visit_page(self, begin_date, end_date):
        """
        访问页面。目前只提供按 page_visit_pv 排序的 top200。
        详情请参考
        https://developers.weixin.qq.com/miniprogram/dev/api/getAnalysisVisitPage.html
        :param begin_date: 起始日期
        :param end_date: 结束日期
        :return: 统计数据列表
        """
        res = self._post(
            'getweanalysisappidvisitpage',
            data={
                'begin_date': self._to_date_str(begin_date),
                'end_date': self._to_date_str(end_date)
            },
            result_processor=lambda x: x['list']
        )
        return res

    def get_analysis_daily_visit_trend(self, begin_date, end_date):
        """
        获取用户访问小程序数据日趋势
        详情请参考
        https://developers.weixin.qq.com/miniprogram/dev/api/getAnalysisDailyVisitTrend.html
        :param begin_date: 起始日期
        :param end_date: 结束日期
        :return: 统计数据列表
        """
        res = self._post(
            'getweanalysisappiddailyvisittrend',
            data={
                'begin_date': self._to_date_str(begin_date),
                'end_date': self._to_date_str(end_date)
            },
            result_processor=lambda x: x['list']
        )
        return res

