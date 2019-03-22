import requests
import baibaoxiang.excel_xlwt
excel=baibaoxiang.excel_xlwt.a()
import re



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