from PIL import Image
from PIL import ImageGrab
import pytesseract
from PIL import Image




box = (53,994, 560,1047)
image = Image.open('D:\img\\2018-09-20--11^29^56进入商品详情页面.png')
newImage = image.crop(box)
newImage.save('a.png')
im=Image.open('a.png')
print(pytesseract.image_to_string (im))
jiage=pytesseract.image_to_string (im)
jiage=float(jiage)
print("商品价格",jiage,"元")

