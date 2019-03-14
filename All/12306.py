import requests
url="https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2019-01-31&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=XFN&purpose_codes=ADULT"
r=requests.get(url)


print(r.status_code)
print(r.text)