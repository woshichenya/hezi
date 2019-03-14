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
          "ufo": {
            "uuid": "1550210850540313295",
            "nickName": "陈雅",
            "province": "",
            "gender": 1,
            "avatarUrl": "https://wx.qlogo.cn/mmopen/vi_32/g358vshZe0FNr19Q1e7M2hq5VyFGmISUkuBGibzrjzvrDQjMxCBYRqkCX9dLExMRvf7yZmcMSYD7RN1rUaic4z0w/132",
            "language": "zh_CN",
            "city": "",
            "country": "中国"
          },
          "ev": "page",
          "uuid": "1550210850540313295",
          "phoneModel": "iPhone 5",
          "userMarker": "15506252426373527013",
          "ag": {
            "id": "251"
          },
          "logtime": "2019-02-20 18:50:26",
          "system": "iOS 10.0.1",
          "SDKVersion": "6.1.2",
          "lastPage": "pages/index/index",
          "eventName": "page",
          "wayScene": {},
          "network": "wifi",
          "winW": 320,
          "wsdk": "1.9.97",
          "ty": 1,
          "@timestamp": "2019-02-20T10:50:26.000Z",
          "rq_c": 4,
          "time": 1550631026378,
          "currentPage": "pages/goods/detail/index",
          "lang": "zh",
          "wxVersion": "6.6.3",
          "errorCount": 0,
          "winH": 456,
          "platform": "devtools",
          "dr": 2,
          "@version": "1",
          "appKey": "80d114e0c97f848e79ecef61a489a940",
          "pixelRatio": 2,
          "life": "show"
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
