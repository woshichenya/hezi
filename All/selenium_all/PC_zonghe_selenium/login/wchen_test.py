# coding: utf-8
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
import baibaoxiang
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

import smtplib
from email.mime.text import MIMEText
from email.header import Header
import femail
import traceback

'''必改参数'''
userid="3482"
url="https://test-sso.vdongchina.com/"
username="vdongshopplus"
# username="18710262651"
# username="18871551774"
pasword="1234567890"
# pasword="123456789"
name="陈雅小号"
shopname="微动商城"

'''web开始'''
GO=baibaoxiang.geturl
Go= baibaoxiang.geturl.llq
go= baibaoxiang.geturl(url)
Go.maximize_window()





def login_40():
    try:
        go.Sxpath("//input[@name='username']","用户名输入框",username,"成功输入用户名","输入用户名失败")
        go.STag_name_zidingyi("input","id","pasword",pasword,"密码输入框","成功输入密码","输入密码失败")
        go.CTag_name_zidingyi("button", "text", "登录","登陆按钮","登录中","无法点击登陆")

    except Exception as e:
        pen_names=go.paizhao_pc("登录报错图片")
login_40()



