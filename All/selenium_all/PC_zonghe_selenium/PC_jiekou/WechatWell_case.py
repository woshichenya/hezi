
import requests
import re


data={
    "avatar":"",
    "bd_qs2ptZ":"",
    "can_lottory":"1",
    "had_sign":"1",
    "isblacklist":"1",
    "mobile":"",
    "nick_name":"ttt2",
    "sex":"1",
    "submit":"提交",
    "token":"2912a6ad",
    "user_id":"",
}
fleads={
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Connection":"keep-alive",
    "Content-Length":"144",
    "Content-Type":"application/x-www-form-urlencoded",
    "Cookie":"Hm_lvt_bd3bd79ac0fdbfdfece9009d7f93e160=1541569762,1542348059,1543560199; _ga=GA1.2.925936411.1541569770; fa9e___lastvisit_12=8%2Chttps%3A//test-sso-xiao.vdongchina.com/web/index.php%3Fc%3Dsite%26a%3Dentry%26do%3Dmy_home%26m%3Dmeepo_xianchang; fa9e_history_url=%5B%7B%22title%22%3A%22%5Cu4f1a%5Cu5458-%5Cu4f1a%5Cu5458%5Cu5217%5Cu8868%22%2C%22url%22%3A%22.%5C%2Findex.php%3Fc%3Dsite%26a%3Dentry%26m%3Dewei_shopv2%26do%3Dweb%26r%3Dmember.list%22%7D%2C%7B%22title%22%3A%22%5Cu4f1a%5Cu5458-%5Cu4f1a%5Cu5458%5Cu5217%5Cu8868%22%2C%22url%22%3A%22.%5C%2Findex.php%3Fc%3Dsite%26a%3Dentry%26m%3Dewei_shopv2%26do%3Dweb%26r%3Dmember.list%22%7D%2C%7B%22title%22%3A%22%5Cu4f1a%5Cu5458-%5Cu4f1a%5Cu5458%5Cu5217%5Cu8868%22%2C%22url%22%3A%22.%5C%2Findex.php%3Fc%3Dsite%26a%3Dentry%26m%3Dewei_shopv2%26do%3Dweb%26r%3Dmember.list%22%7D%2C%7B%22title%22%3A%22%5Cu4f1a%5Cu5458-%5Cu4f1a%5Cu5458%5Cu5217%5Cu8868%22%2C%22url%22%3A%22.%5C%2Findex.php%3Fc%3Dsite%26a%3Dentry%26m%3Dewei_shopv2%26do%3Dweb%26r%3Dmember.list%22%7D%2C%7B%22title%22%3A%22%5Cu652f%5Cu4ed8%5Cu8bbe%5Cu7f6e%22%2C%22url%22%3A%22.%5C%2Findex.php%3Fc%3Dsite%26a%3Dentry%26m%3Dewei_shopv2%26do%3Dweb%26r%3Dsysset.payset%22%7D%2C%7B%22title%22%3A%22%5Cu57fa%5Cu7840%5Cu8bbe%5Cu7f6e%22%2C%22url%22%3A%22.%5C%2Findex.php%3Fc%3Dsite%26a%3Dentry%26m%3Dewei_shopv2%26do%3Dweb%26r%3Dsysset.shop%22%7D%2C%7B%22title%22%3A%22%5Cu652f%5Cu4ed8%5Cu7ba1%5Cu7406%22%2C%22url%22%3A%22.%5C%2Findex.php%3Fc%3Dsite%26a%3Dentry%26m%3Dewei_shopv2%26do%3Dweb%26r%3Dsysset.payment%22%7D%2C%7B%22title%22%3A%22%5Cu9500%5Cu552e%5Cu7edf%5Cu8ba1%22%2C%22url%22%3A%22.%5C%2Findex.php%3Fc%3Dsite%26a%3Dentry%26m%3Dewei_shopv2%26do%3Dweb%26r%3Dstatistics.sale%22%7D%2C%7B%22title%22%3A%22%5Cu5e94%5Cu7528-%5Cu5e94%5Cu7528%22%2C%22url%22%3A%22.%5C%2Findex.php%3Fc%3Dsite%26a%3Dentry%26m%3Dewei_shopv2%26do%3Dweb%26r%3Dplugins%22%7D%2C%7B%22title%22%3A%22%5Cu8ba2%5Cu5355-%5Cu5f85%5Cu6536%5Cu8d27%22%2C%22url%22%3A%22.%5C%2Findex.php%3Fc%3Dsite%26a%3Dentry%26m%3Dewei_shopv2%26do%3Dweb%26r%3Dorder.list.status2%22%7D%5D; fa9e___lastvisit_1=8%2Chttps%3A//test-sso-xiao.vdongchina.com/web/index.php%3Fc%3Dplatform%26a%3Dreply%26m%3Dmeepo_xianchang%26version_id%3D0; fa9e___lastvisit_799=8%2Chttps%3A//test-sso-xiao.vdongchina.com/web/index.php%3Fc%3Dmodule%26a%3Dmanage-account; __lastvisit_799=8%2Chttps%3A//test-sso-xiao.vdongchina.com/web/index.php%3Fc%3Dsite%26a%3Dentry%26m%3Dewei_shopv2%26do%3Dweb%26r%3Dmember.list%26time%255Bstart%255D%3D%26time%255Bend%255D%3D%26followed%3D%26level%3D%26groupid%3D%26isblack%3D%26realname%3D%25E9%2599%2588%25E9%259B%2585; __lastvisit_1=8%2Chttps%3A//test-sso-xiao.vdongchina.com/web/index.php%3Fc%3Dsite%26a%3Dentry%26m%3Dewei_shopv2%26do%3Dweb%26r%3Dsysset.payset; __notice=1545064004; fa9e___notice=1545064072; PHPSESSID=588c584c2cba30769be686d6d7da377e; fa9e___lastvisit_756=8%2Chttps%3A//test-sso-xiao.vdongchina.com/web/index.php%3Fc%3Dsite%26a%3Dentry%26do%3Dredpack_wallet%26m%3Dmeepo_xianchang; fa9e_module_status:meepo_xianchang=%7B%22upgrade%22%3A%7B%22upgrade%22%3A0%7D%2C%22ban%22%3A0%7D; fa9e_module_status:ewei_bigwheel=%7B%22upgrade%22%3A%7B%22upgrade%22%3A0%7D%2C%22ban%22%3A0%7D; test_wd_token=a982599b4d42938585549fc013ada1ba; fa9e__status=%7B%22uid%22%3A%22799%22%2C%22username%22%3A%2218871551774%22%7D; fa9e___session=887eCI9juj0v2PBV9fyw%2BInthBORFoQuJngAhzpt7cgt8angoGZWztWdL1v89ssVQlXTg2BTJJuVScTTPdgxgXYS1JLBddKWdWgufetBqQjjQcNsMvXBbhwTliUX94cbLnZc5aytMFtEgzCuX%2BvwSQwAUfhJDnaVeFxlLSCc8Jna9dyVIg; fa9e___uniacid=8; fa9e___switch=VLKv1; fa9e___uid=799",
    "Host":"test-sso-xiao.vdongchina.com",
    "Referer":"https://test-sso-xiao.vdongchina.com/web/index.php?c=site&a=entry&op=post&id=32&do=user_manage&m=meepo_xianchang",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0",

}
url="https://test-sso-xiao.vdongchina.com/web/index.php?c=site&a=entry&op=post&id=32&do=user_manage&m=meepo_xianchang"

k=requests.post(url, data=data, headers=fleads)

print(k.text)
