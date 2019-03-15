#!/usr/bin/env python
# -*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: mage
# Mail: mage@woodcol.com
# Created Time: 2018-1-23 19:17:34
#############################################


from setuptools import setup, find_packages

setup(
    name="chenyabaibaoxiang",
    version="2.1.0",
    keywords=("dashu", "baibaoxiang"),
    description="time and path tool",
    long_description="time and path tool",
    license="MIT Licence",

    url="https://www.baidu.com",
    author="dashu",
    author_email="bj_xiaoya@163.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
	install_requires=[]
    #install_requires=["selenium","wheel","xlwt","pymysql","smtplib","pillow","pytesseract","requests","traceback"]
)