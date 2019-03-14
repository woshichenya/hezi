# -*- coding: utf-8 -*-
import configparser


class getConfig():
    def __init__(self):
        #self.path = 'myConfig/myConfig.ini'          #########路径需要改一下
        #self.path_interface = "myConfig/interfaceConfig.ini"  #########路径需要改一下
        self.path = 'G:\\autoTestInterface\\interfaceTest\\myConfig\\myConfig.ini'          #########路径需要改一下
        self.path_interface = "G:\\autoTestInterface\\interfaceTest\\myConfig\\interfaceConfig.ini"  #########路径需要改一下

    def get_excelname(self):
        configPath = self.path
        config = configparser.ConfigParser()
        config.read(configPath)
        value = config.get("EXCEL", "excelname")
        return value

    def get_privatekey(self):
        configPath = self.path
        config = configparser.ConfigParser()
        config.read(configPath)
        value = config.get("PRIVATEKEY", "myPrivateKey")
        return value
    def get_sheetnum(self):
        configPath = self.path
        config = configparser.ConfigParser()
        config.read(configPath)
        value = config.get("SHEETNUM", "sheetnum")
        return value
    def get_newexcelname(self):
        configPath = self.path
        config = configparser.ConfigParser()
        config.read(configPath)
        value = config.get("NEWEXCEL", "newexcelname")
        return value
    def get_url(self):
        configPath = self.path
        config = configparser.ConfigParser()
        config.read(configPath)
        value = config.get("HTTPS", "url")
        return value

    def get_interface(self,section,key):
        configPath = self.path_interface
        config = configparser.ConfigParser()
        config.read(configPath)
        value = config.get(section, key)
        return value










    def set_newexcelname(self,value):
        configPath = self.path
        config = configparser.ConfigParser()
        config.read(configPath)
        config.set("NEWEXCEL","newexcelname",value)
        config.write(open(configPath, "w"))






'''
my_test = getConfig()
test1 = my_test.get_excelname()
test2 = my_test.get_privatekey()
test222=my_test.get_interface1()
test333=my_test.get_interface2()
print(test1)
print(test2)
print(test222)
print(test333)
'''