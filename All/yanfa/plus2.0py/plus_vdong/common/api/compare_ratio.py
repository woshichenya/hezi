# -*- coding: UTF-8 -*-
# 计算日同比周环比
class CompareRatio(object):

    def compare(self):

        return {
            self.field+"_tongbi":self.week_compare(),
            self.field + "_huanbi":self.day_compare(),
        }

    #周同比
    def week_compare(self):
        # 本期
        current_period_data = float(self.current_period_data())
        #同期
        the_corresponding_period_data = self.week_the_corresponding_period_data()
        if not the_corresponding_period_data:
            return "--"
        data = ((current_period_data - the_corresponding_period_data) / the_corresponding_period_data)*100
        data = float('%.1f' % data)
        return str(data)+"%"
    #入环比
    def day_compare(self):
        # 本期
        current_period_data = float(self.current_period_data())
        # 同期
        the_corresponding_period_data = self.day_the_corresponding_period_data()

        if not the_corresponding_period_data:
            return "--"
        data = ((current_period_data - the_corresponding_period_data) / the_corresponding_period_data) * 100
        data = float('%.1f' % data)
        return str(data) + "%"

    def current_period_data(self, **kwargs):
        return 0


    def week_the_corresponding_period_data(self, **kwargs):
        return 0

    def day_the_corresponding_period_data(self, **kwargs):
        return 0