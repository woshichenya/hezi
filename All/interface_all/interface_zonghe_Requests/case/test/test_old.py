import re
c={
    "appKey":"app_key",
    "uuid":"用户唯一标示",
    "openId":"用户openid",
    "ufo":"用户信息",
    "wayScene":"路径+参数场景值（小程序show回调返回的参数）",
    "userMarker":"session标识（入口token）",
    "time":"开始的时间",
    "pointName":"事件名称（自定义事件埋点事件名称）",
    "eventName":"埋点的事件类型",
    "SDKVersion":"sdk版本",
    "dr":"",
    "currentPage":"当前页面的路径",
    "network":"网络类型",
    "phoneModel":"手机型号",
    "life":"小程序生命周期",
    "shareCount":"分享当前页面的次数",
    "errorCount":"错误数量",
    "eventTime":"当前请求的时间",
    "pixelRatio":"像素点",
    "winW":"屏幕宽度",
    "winH":"屏幕高度",
    "lang":"浏览器语言",
    "wxVersion":"微信版本号",
    "lat":"经度",
    "lng":"纬度",
    "speed":"速度",
    "system":"系统版本",
    "platform":"客户端平台",
    "pc":"page_count",
    "fp":"first_page",
    "lastPage":"上个页面的路径",
    "is_first_page":"是不是第一个页面",
    "ln":"location_name",
    "ct":"",
    "sr":"",
    "qr":"",
    "usr":"",
    "la_c":"",
    "as_c":"",
    "ah_c":"",
    "rq_c":"第几次请求",
    "ag":"当前页面的参数",
    "avatarUrl":"用户微信头像地址",
    "city":"市",
    "country":"国家",
    "gender":"性别（ 0：未知、1：男、2：女）",
    "language":"语言",
    "nickName":"微信昵称",
    "province":"省",
    "rq_c":"第几次请求",
    "uuid":"用户唯一标示",
    "openid":"用户openid",



}
a={
  "took": 2,
  "timed_out": "false",
  "_shards": {
    "total": 5,
    "successful": 5,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": 4,
    "max_score": 1,
    "hits": [
      {
        "_index": "logstash-1-536-page-2019-03-15",
        "_type": "doc",
        "_id": "0AsCf2kBiZy68uZC3zlL",
        "_score": 1,
        "_source": {
          "eventTime": 1552614086255,
          "@version": "1",
          "@timestamp": "2019-03-15T09:41:26.000Z",
          "system": "iOS 10.0.1",
          "platform": "devtools",
          "ty": 1,
          "logtime": "2019-03-15 17:41:26",
          "winH": 555,
          "pixelRatio": 2,
          "time": 1552614086202,
          "dr": 0,
          "userMarker": "15526140862112049640",
          "fp": 0,
          "winW": 375,
          "lang": "zh",
          "la_c": 2,
          "phoneModel": "iPhone 6",
          "pc": 1,
          "wsdk": "1.9.97",
          "ah_c": 0,
          "ev": "app",
          "errorCount": 0,
          "rq_c": 2,
          "life": "launch",
          "ufo": {},
          "uuid": "15517525665583054408",
          "wayScene": {},
          "appKey": "536",
          "SDKVersion": "6.1.2",
          "eventName": "page",
          "as_c": 0
        }
      },
      {
        "_index": "logstash-1-536-page-2019-03-15",
        "_type": "doc",
        "_id": "VwUCf2kBQ3rQFs4b8kdM",
        "_score": 1,
        "_source": {
          "@version": "1",
          "@timestamp": "2019-03-15T09:41:33.000Z",
          "ct": 1,
          "logtime": "2019-03-15 17:41:33",
          "ty": 1,
          "winH": 555,
          "pixelRatio": 2,
          "wxVersion": "6.6.3",
          "network": "2g",
          "time": 1552614093268,
          "lang": "zh",
          "userMarker": "15526140862112049640",
          "winW": 375,
          "phoneModel": "iPhone 6",
          "ev": "event",
          "rq_c": 5,
          "pointName": "vdong_reachbottom",
          "ufo": {
            "language": "zh_CN",
            "province": "北京",
            "uuid": "15517525665583054408",
            "country": "中国",
            "nickName": "都是佚名",
            "city": "昌平",
            "avatarUrl": "https://wx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTIRdRic7Jujz7fibvLrk4QYh5tVatpNicfLWg96YsicG1fPhCt01ZyL4NpXmG5RK1TjRCqtLR2bZeWlzg/132",
            "gender": 2
          },
          "openId": "osX135I4GC6M8n2a-6hsPaWDBreA",
          "uuid": "15517525665583054408",
          "wayScene": {},
          "appKey": "536",
          "eventName": "page",
          "SDKVersion": "6.1.2"
        }
      },
      {
        "_index": "logstash-1-536-page-2019-03-15",
        "_type": "doc",
        "_id": "0QsCf2kBiZy68uZC3zlL",
        "_score": 1,
        "_source": {
          "@version": "1",
          "@timestamp": "2019-03-15T09:41:27.000Z",
          "system": "iOS 10.0.1",
          "platform": "devtools",
          "ty": 1,
          "logtime": "2019-03-15 17:41:27",
          "winH": 555,
          "pixelRatio": 2,
          "wxVersion": "6.6.3",
          "isFirstPage": "true",
          "network": "2g",
          "time": 1552614087170,
          "dr": 3,
          "userMarker": "15526140862112049640",
          "winW": 375,
          "lang": "zh",
          "phoneModel": "iPhone 6",
          "wsdk": "1.9.97",
          "ev": "page",
          "errorCount": 0,
          "currentPage": "pages/index/index",
          "rq_c": 3,
          "life": "show",
          "ufo": {
            "language": "zh_CN",
            "province": "北京",
            "uuid": "15517525665583054408",
            "country": "中国",
            "nickName": "都是佚名",
            "city": "昌平",
            "avatarUrl": "https://wx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTIRdRic7Jujz7fibvLrk4QYh5tVatpNicfLWg96YsicG1fPhCt01ZyL4NpXmG5RK1TjRCqtLR2bZeWlzg/132",
            "gender": 2
          },
          "uuid": "15517525665583054408",
          "wayScene": {},
          "appKey": "536",
          "eventName": "page",
          "SDKVersion": "6.1.2"
        }
      },
      {
        "_index": "logstash-1-536-page-2019-03-15",
        "_type": "doc",
        "_id": "0wsCf2kBiZy68uZC5jlr",
        "_score": 1,
        "_source": {
          "@version": "1",
          "@timestamp": "2019-03-15T09:41:30.000Z",
          "system": "iOS 10.0.1",
          "platform": "devtools",
          "ty": 1,
          "logtime": "2019-03-15 17:41:30",
          "winH": 555,
          "pixelRatio": 2,
          "wxVersion": "6.6.3",
          "network": "2g",
          "time": 1552614090166,
          "dr": 20,
          "userMarker": "15526140862112049640",
          "winW": 375,
          "lang": "zh",
          "ag": {
            "id": "410"
          },
          "phoneModel": "iPhone 6",
          "wsdk": "1.9.97",
          "lastPage": "pages/index/index",
          "ev": "page",
          "errorCount": 0,
          "currentPage": "pages/goods/detail/index",
          "rq_c": 4,
          "life": "show",
          "ufo": {
            "language": "zh_CN",
            "province": "北京",
            "uuid": "15517525665583054408",
            "country": "中国",
            "nickName": "都是佚名",
            "city": "昌平",
            "avatarUrl": "https://wx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTIRdRic7Jujz7fibvLrk4QYh5tVatpNicfLWg96YsicG1fPhCt01ZyL4NpXmG5RK1TjRCqtLR2bZeWlzg/132",
            "gender": 2
          },
          "uuid": "15517525665583054408",
          "wayScene": {},
          "appKey": "536",
          "eventName": "page",
          "SDKVersion": "6.1.2"
        }
      }
    ]
  }
}

b={"uuid":"1550210850540313295","userMarker":"15506252426373527013","wayScene":{},"appKey":"80d114e0c97f848e79ecef61a489a940","eventName":"page","time":1550631026378,"dr":2,"currentPage":"pages/goods/detail/index","life":"show","errorCount":0,"network":"wifi","phoneModel":"iPhone 5","pixelRatio":2,"winW":320,"winH":456,"lang":"zh","wxVersion":"6.6.3","SDKVersion":"6.1.2","wsdk":"1.9.97","system":"iOS 10.0.1","platform":"devtools","lastPage":"pages/index/index","ag":{"id":"251"},"rq_c":4,"ufo":{"nickName":"陈雅","gender":1,"language":"zh_CN","city":"","province":"","country":"中国","avatarUrl":"https://wx.qlogo.cn/mmopen/vi_32/g358vshZe0FNr19Q1e7M2hq5VyFGmISUkuBGibzrjzvrDQjMxCBYRqkCX9dLExMRvf7yZmcMSYD7RN1rUaic4z0w/132","uuid":"1550210850540313295"}}

print("数据采集系统收到的值有%s个"%len(a))
print("埋点上传的值有%s个"%len(b))
print("*"*200)
sum = 0
sum2=0
for x in a :
    if x in b :
        sum +=1
    else:
        if x in c:
            sum2+=1
        try:
            print("数据采集系统中是：", x, ":", a[x],"埋点上传的内容是",x,":",b[x])
        except:
            try:
                print("数据采集系统中是：",x,":",a[x])
            except:
                print("数据采集系统中没有",x)
            try:
                print("埋点上传的内容是",x,":",b[x])
            except:
                print("埋点上传中没有", x)
print("*" * 200)
print("后台和埋点数据不一致的有%s个"%(len(a)-sum))
print("不一致且不在表格中的有%s个"%sum2)
print("*" * 200)
sum=0
for ss in c :
    if ss not in b:
        if ss not in b["ufo"]:
            sum+=1
            print("缺少字段",ss,"-----翻译：",c[ss])
print("埋点没有上传的数据有%s个"%sum)


s=str(a)
print(s)
sss=re.findall("\'openId\':\ '(.*?)\'",s)
print(sss)
print(len(sss))
sy=set(sss)
print(sy)