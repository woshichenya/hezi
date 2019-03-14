from PIL import Image
import pytesseract
import traceback

'''封装一个获取文本的方法'''
st=[]
def get_shoping_img_jiage():
    try:
        im = Image.open('b.png')
        int=pytesseract.image_to_string(im,lang='chi_sim')#获取打开的图片，并加上参数chi_sim,将图片中解析的数字赋值给int
        print("数字",int)
        im = Image.open('a.png')
        text= pytesseract.image_to_string(im,lang='chi_sim')#获取打开的图片，并加上参数chi_sim,将图片中解析的文字赋值给text
        print("汉字",text)
        print("输出第二个字符:",text[0])
        text_a=text.replace(" ","")#去掉空格
        print(text_a)
    except Exception as e:
        ee = traceback.format_exc()
        print(ee)
get_shoping_img_jiage()