'''定义一个基础数组'''
aa={
    "a":1,
    "b":2,
    "c":3,
}
print(aa['b'])
huiyuan_zehou={
    "普通会员":1,
    "钻石会员":0.77,
    "白银会员":1,
    "黄金会员":1
}
print(aa)
print(aa['a'])

'''定义一个扩展数组'''
bb={
    "d":4,
    "e":5
}
print(aa)
'''将bb字典添加到aa中'''
aa.update(bb)
print(aa)
'''添加一个元素：f=6'''
aa.update(f=6)
print(aa)
'''添加一个元素：g=7'''
aa.update({'g':7})
print(aa)
'''删除一个元素：g'''
aa.pop('g')
print(aa)


t=[]
t.append("a")
print(t)
