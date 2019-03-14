import requests
import re
import xlwt
import time
#只能写不能读
class a:
    biaoti=["接口名称","接口地址","接口参数","响应状态","返回值"]
    book = xlwt.Workbook()  # 新建一个excel
    sheet1 = book.add_sheet('case1_sheet')#添加一个sheet页
    book = xlwt.Workbook()  # 新建一个excel
    sheet1 = book.add_sheet('case1_sheet')  # 添加一个sheet页
    row = 0  # 控制行
    col = 0  # 控制列
    for stu in biaoti:
        # print(stu)
        sheet1.write(row, col, stu)
        col += 1
    row += 1
    col = 0  # 控制列
    # print(row, col)
    # sheet1.write(11, 0, '12344444')


    def input_excel(self,k):
        # print(k)
        for kk in k:
            # print(kk)
            a.sheet1.write(a.row, a.col, kk)
            a.col += 1
        a.row += 1
        a.col = 0  # 控制列
        # print(a.row,a.col)


    def end(self,name):
        tt=time.strftime("%Y%m%d%H%M%S",time.localtime())
        a.book.save("D:\linshi\\test22\\"+tt+name+".xls")  # 保存到当前目录下



excel=a()

class go:
    hang = 0
    lie = 0

    def leiji(self):
        # print(go.k, ",", go.l)
        go.lie += 1
        if go.lie >= 3:
            go.hang += 1
            go.lie = 0
    def __init__(self):
        print("开始接口连接过程。。。")



    def post(self,url, data, header,name):

        r = requests.post(url, data=data, headers=header)
        if "\"msg\":\"ok\"" in r.text and r.status_code == 200:
            print(name,"成功")
            try:
                print(r.json())
            except:
                print("无法输出json，转换成输出text")
                print(r.text)
            # fanhui=re.findall("\{\"code\":.*?.*",r.text)
            # # print("这里是数组*************************", fanhui)
            # if len(fanhui) == 0:
            #     fanhui = re.findall("\{\'code\':.*?.*",r.text)
            #     if len(fanhui) == 0:
            #         fanhui=r.text
            # jieguo=[name,url,str(data),r.status_code,fanhui]
            # excel.input_excel(jieguo)


        else:
            print(name,"未成功*****************************************************************************")
            try:
                print(r.json())
                fanhui = re.findall("\{\"code\":.*?.*", str(r.json()))
                # print("这里是数组*************************",fanhui)
                if len(fanhui) == 0:
                    fanhui = re.findall("\{\'code\':.*?.*", str(r.json()))
                    if len(fanhui) == 0:
                        fanhui = str(r.json())
                jieguo = [name, url, str(data), r.status_code, fanhui]
                excel.input_excel(jieguo)
            except:
                print("无法输出json，转换成输出text")
                print(r.text)
                fanhui = re.findall("\{\"code\":.*?.*", r.text)
                # print("这里是数组*************************", fanhui)
                if len(fanhui) == 0:
                    fanhui = re.findall("\{\'code\':.*?.*", r.text)
                    if len(fanhui) == 0:
                        fanhui = r.text
                jieguo = [name, url, str(data), r.status_code, fanhui]
                excel.input_excel(jieguo)
        return r

    def shoujihao(self):
        # shouji_txt = open(r'..\case\shoujihao.txt')
        shouji_txt = open(r'..\..\case\shoujihao.txt')
        shouji = int(shouji_txt.read())
        t = shouji + 1
        shouji_txt.close()
        # shouji_txt = open("..\case\shoujihao.txt", 'w')
        shouji_txt = open("..\shoujihao.txt", 'w')
        x = str(t)
        shouji_txt.write(x)
        shouji_txt.close()
        return shouji