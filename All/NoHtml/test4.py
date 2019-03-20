# coding:utf-8
from selenium import webdriver

driver = webdriver.PhantomJS(executable_path='D:\job\software\phantomJs\phantomjs-2.1.1-windows\\bin\phantomjs.exe')
driver.get('https://www.baidu.com')
print('页面标题：', driver.title)  # 页面标题
print(driver.current_url)  # 当前页面url
elem = driver.find_element_by_id('kw')
elem.send_keys(u'php')
# elem.send_keys(Keys.ENTER)  #点击键盘上的Enter按钮
driver.find_element_by_id('su').click()  # 点击了百度页面上的‘百度一下’按钮
driver.refresh()
print('页面标题：', driver.title)  # 页面标题
print(driver.current_url)  # 当前页面url
# print('搜索后的页面源码：\n', driver.page_source)  # 页面源码