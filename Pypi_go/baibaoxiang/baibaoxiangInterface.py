import requests
import re
from baibaoxiang import excel
import ast


class go:
    hang = 0
    lie = 0
    excel_input=excel.InputExcel()
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
                go.excel_input.input_excel(jieguo)
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
                go.excel_input.input_excel(jieguo)
        return r

    def get(self,url, data, header,name):
        r = requests.get(url, data=data, headers=header)
        if "\"msg\":\"ok\"" in r.text and r.status_code == 200:
            print(name,"成功")
            try:
                print(r.json())
            except:
                print("无法输出json，转换成输出text")
                print(r.text)
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
                go.excel_input.input_excel(jieguo)
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
                go.excel_input.input_excel(jieguo)
        return r



class Interface_go:
    def interface_go(self,open_excel_file_address,input_excel_name,input_excel_address):
        i=go()
        goi=excel.OpenExcel()
        # t=go.open_excel('D:\linshi\涉及鲜橙收入和金额收入接口.xlsx')
        # t=go.open_excel('D:\linshi\工作簿1.xlsx')
        try:
            t=goi.open_excel(open_excel_file_address)
        except:
            print("文件地址必须是单引号")
        # print(t)
        for x in t:
            # print(x)
            name=x[0]
            address="http://"+x[1]+x[2]
            # print(x[3])
            try:
                data=ast.literal_eval(x[3])
            except:
                print("表格中的参数，必须加上双引号")
            # print(name+"\n"+address)
            # print(data)
            healer={}
            if x[5]=="post":
                i.post(address,data,healer,name)
            if x[5]=="get":
                i.get(address,data,healer,name)
        # excel.InputExcel().end("D:\\linshi\\","特殊")
        excel.InputExcel().end(input_excel_address,input_excel_name)
