import requests

url = "http://test-plus.moliyan.com.cn/api/group/Saveheadurl"

payload = " form-data; name=\"token\"\r\n\r\neyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJwbHVzIiwiaWF0IjoxNTQ1ODk0ODEzLCJleHAiOjE1NDU5MDIwMTMsInVpZCI6Ijg3MyJ9.v6ienoYilB16TmG6Cc2m4GLAUBc5gym-jgTj6o8x3-s\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"headpic\"; filename=\"G:\\工作文件\\截图\\1功能探索订阅号1.jpg\"\r\nContent-Type: image/jpeg\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"


response = requests.request("POST", url, data=payload,)

print(response.text)