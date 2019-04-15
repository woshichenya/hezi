import ast
'''定义一个基础数组'''
aa={
    "a":1,
    "b":2,
    "c":3,
}
print("显示aa字典的b标签",aa['b'])
huiyuan_zehou={
    "普通会员":1,
    "钻石会员":0.77,
    "白银会员":1,
    "黄金会员":1
}
print("显示aa字典",aa)
print("显示aa字典的b标签",aa['a'])

'''定义一个扩展数组'''
bb={
    "d":4,
    "e":5
}
print(aa)
'''将bb字典添加到aa中'''
aa.update(bb)
print("将bb字典添加到aa中",aa)
'''添加一个元素：f=6'''
aa.update(f=6)
print("添加一个元素：f=6",aa)
'''添加一个元素：g=7'''
aa.update({'g':7})
print("添加一个元素：g=7",aa)
'''删除一个元素：g'''
aa.pop('g')
print("删除一个元素：g",aa)

t=[]
t.append("a")
print("给数组添加元素",t)
x="{num:1,id:1,user_id:1}"

k='{"num":1,"id":1,"user_id":1,"name":"ttt"}'
print(k)
k3=ast.literal_eval(k)
print("直接拆分成字典：",k3)
k=k[1:len(k)-1]
print("去掉头尾：",k)
k1=k.split(",")
print("拆分成数组",k1)
k6={}
for k4 in k1:
    print(k4)
    k5=k4.split(":")
    print(k5)
    k6[k5[0]]=k5[1]
print(k6)

