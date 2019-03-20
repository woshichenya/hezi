from selenium import webdriver
from selenium.webdriver.chrome.options import Options
u="https://www.baidu.com"
chrome_options=Options()
chrome_options.add_argument('--headless')
go=webdriver.Chrome(chrome_options=chrome_options)
go.get(u)
print(go.page_source)
go.close()
go.quit()

# k=webdriver.Firefox()
# k.close()
# l=webdriver.Chrome()
# l.get("http://www.baidu.com")