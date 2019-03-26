
from selenium import webdriver
from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 600))
display.start()


options = webdriver.ChromeOptions()
options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=options)
browser.get("http://www.baidu.com")
print(browser.page_source)
browser.quit()
display.stop()