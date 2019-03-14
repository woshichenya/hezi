import baibaoxiangInterface
go=baibaoxiangInterface.go()
url="http://39.107.239.18:5601/api/console/proxy"
data={
    "method":"GET",
    "path":"/logstash-1-80d114e0c97f848e79ecef61a489a940-page-2019-02-19/doc/_search"
}
headers={
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Connection":"keep-alive",
    "Content-Length":"0",
    "Host":"39.107.239.18:5601",
    "kbn-version":"6.3.2",
    "Referer":"http://39.107.239.18:5601/app/kibana",
    "User-Agent":"Mozilla/5.0 Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0",
}
r=go.post(url,data,headers,"获取当天数据")
# print(r.headers)

print("*"*200)