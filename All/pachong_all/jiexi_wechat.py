#__author: xlu.com
#date : 2018/10/25

import requests
from urllib import request
import re
import pymysql
import os
import threading
from  queue import Queue
#from lxml import etree



# from pymysql import connections
head = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
# 使用re抽取内容
def getContentByUrl(url):
    resp = requests.get(url,headers=head)
    html = resp.content.decode('utf-8')
    # icon
    icon = re.findall(r'<div class="detailLeft fl">.*?<div class="img fl">(.*?)</div>',html,re.DOTALL)
    # 没有过滤掉没有icon的
    if len(icon)<1:
        return 0
    icon = re.findall(r'src="(.*?)"',icon[0],re.DOTALL)
    #名称
    name = re.findall(r'<div class="detailLeft fl">.*?<div class="dataList fl">.*?<div class="clear">.*?<h3 class="fl">(.*?)</h3>.*?</div>',html,re.DOTALL)
    #二维码
    erweima = re.findall(r'<div class="detailLeft fl">.*?<div class="detaltext">.*?<img src="(.*?)".*?</div>',html,re.DOTALL)
    #描述
    desc = re.findall(r'<div class="detailLeft fl">.*?<div class="detaltext">.*?<div class="lite-code fr">.*?<h3>.*?<p>(.*?)</p>.*?</div>',html,re.DOTALL)
    #描述图
    imgs = re.findall(r'<div class="detailLeft fl">.*?<div class="detaltext">.*?<ul class="imgsroll clear">(.*?)</ul>.*?</div>',html,re.DOTALL)
    if len(imgs)>0:
        imgs = re.findall(r'src="(.*?)"',imgs[0],re.DOTALL)
        imgs = ';'.join(imgs)

    it = {}
    it['icon'] = icon[0]
    it['name'] = name[0]
    it['erweima'] = erweima[0]
    it['desc'] = desc[0]
    it['m_desc'] = desc[0][0:15]
    it['imgs'] = imgs
    return it


def dnowloadimg(path,filename):
    res = request.urlretrieve(path,'img/'+filename)
'''
def main():
    ress = []
    #db = pymysql.connect(host='127.0.0.1',user='root',password='chenlip',database='jjccdb',port=3306)
    db = pymysql.connect(host='39.107.239.18',user='root',password='wdtx.2016',database='vd_moli_test',port=3306)
    cur = db.cursor()
    for i in range(1,12000):
        url = 'http://xcx.9.cn/app/%d' % (i)
        res = getContentByUrl(url)
        if res:
            try:
                #下载icon
                # iconname = os.path.basename(res['icon'])
                # dnowloadimg(res['icon'],iconname)
                # res['icon'] = iconname
                # print(iconname)
                # exit()
                #下载二维码
                # erweima_name = os.path.basename(res['erweima'])
                # dnowloadimg(res['erweima'],erweima_name)
                # res['erweima'] = erweima_name
                # ress.append(res)
                # insert = """insert into pc_wechar(icon,`name`,erweima,`desc`,imgs) values("%s","%s","%s","%s","%s")""" % (res['icon'],res['name'],res['erweima'],res['desc'],res['imgs'])
                insert = """insert into cmf_program(img,`name`,qrcode,`describe_substr`,heat) values("%s","%s","%s","%s","%d")""" % (res['icon'],res['name'],res['erweima'],res['m_desc'],i)
                cur.execute(insert)
                cur.execute("select last_insert_id();")
                data = cur.fetchall();
                mainid = data[0][0]
                subinsert = """insert into cmf_program_info(pid,`describe`,`screenshot`,qq) values("%s","%s","%s","%s")""" % (mainid,res['desc'],res['imgs'],i)
                cur.execute(subinsert)
                db.commit()
            except Exception as e:
                print('%d失败!'%(i))
                continue
        else:
            print('%d不存在!'%(i))
            continue

if __name__ == '__main__':
    main()
    
    
    '''