import configparser

a=2
ini=configparser.ConfigParser()
ini.add_section("aaa")
ini.set("aaa","v1","value")

with open('gogogo.ini', 'w') as fw:
    ini.write(fw)

ini.set("aaa", "v2", "value")
ini.set("aaa", "txt", "3")

with open('gogogo.ini', 'w') as fw:
    ini.write(fw)


