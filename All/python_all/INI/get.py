import configparser
ini=configparser.ConfigParser()

ini.readfp(open("gogogo.ini"))
a=ini.getint("aaa","txt")
a=a+1
print(a)

ini.clear()

ini.add_section("aaa")
ini.set("aaa","txt","6")
with open('gogogo.ini','w') as fw:
    ini.write(fw)