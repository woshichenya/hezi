# -*- coding: UTF-8 -*-
# **  文件名称：local_geocoder.py
# **  功能描述：地理位置逆向
# **
# **  创建者:   Yunlong.Zhao zhaoyunlong@vdongchina.com
# **  创建日期: 2018/10/24 17:20

import sys

from plus_vdong.utils import es_utils

sys.path.append("..")
reload(sys)
sys.setdefaultencoding('utf-8')


def geocoder(lat,lng):
    appkey = '3kpmGYiCw1Vnx1G13C8HQyn2smUUl7nd'
    url = 'http://api.map.baidu.com/geocoder/v2/?output=json&location=%s,%s&output=json&pois=1&ak=%s' % (lat,lng,appkey)
    result_json = es_utils.get_request(url)
    province = result_json["result"]["addressComponent"]["province"]
    city = result_json['result']['addressComponent']['city']
    return province,city


if __name__ == "__main__":
    res = geocoder("40.22077","116.23128")
    print res[0]
    print res[1]
    print res


