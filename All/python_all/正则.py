import re
'''查找数字'''
pattern = re.compile(r'\d+')
result1 = pattern.findall('a3211b123 google 456')
print(result1)
result2 = pattern.findall('run88oob123google456', 0, 10)
print(result2)
rs1=re.findall(r'\d+',"a1b2 c3 4 d5")
print(rs1)

'''查找空格'''
rs2=re.findall(r'\s+',"a1b2 c3 4 d5    ")
print(rs2)

'''部分匹配'''
rs3=re.findall(r'c...',"a1b2 c3 4 d5    ")
print(rs3)
rs3=re.findall(r'c..',"a1b2 c3 4 d5    ")
print(rs3)
rs3=re.findall(r'c.',"a1b2 c3 4 d5    ")
print(rs3)
rs3=re.findall(r'c..4',"a1b2 c3 4 d5 c3 5   ")
print(rs3)
rs3=re.findall(r'c(..)5',"a1b2 c3 4 d5 c3 5   ")
print(rs3)
rs3=re.findall(r'c(.*)5',"a1b2 c3 ccc4 d5 c3 5   ")
print("第一个c到最后一个5之间的字符：",rs3)
rs3=re.findall(r'c.*5',"a1b2 c3 ccc4 d5 c3 5   ")
print("从第一个c到最后一个5的字符：",rs3)
rs3=re.findall(r'c(.*?)5',"a1b2 c3 4 d5 c3 5   ")
print("不包含搜索字段：",rs3)
rs3=re.findall(r'c.*?5',"a1b2 c3 4 d5 c3 5   ")
print("包含搜索字段：",rs3)








