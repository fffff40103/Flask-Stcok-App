
import requests
from bs4 import BeautifulSoup
headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
response=requests.get("https://tw.stock.yahoo.com/quote/2330",headers=headers)
soup=BeautifulSoup(response.text,"html.parser")

stock_name=soup.find('h1',class_="C($c-link-text) Fw(b) Fz(24px) Mend(8px)").text
stock_number=soup.find('span',class_="C($c-icon) Fz(24px) Mend(20px)").text
stock_deal=soup.find("span",class_="Fw(600) Fz(16px)--mobile Fz(14px) D(f) Ai(c)").text


print(stock_name)
print(stock_number)
print(stock_deal)

open=soup.find("span",class_="Fw(600) Fz(16px)--mobile Fz(14px) D(f) Ai(c)").text

#heightest price
height_up=soup.find("span",class_="Fw(600) Fz(16px)--mobile Fz(14px) D(f) Ai(c) C($c-trend-up)")
height_down=soup.find("span",class_="Fw(600) Fz(16px)--mobile Fz(14px) D(f) Ai(c) C($c-trend-down)")
if height_up:
    print(height_up.text)
else:
    print(height_down.text)

#lowest price
low_low=soup.find("span",class_="Fw(600) Fz(16px)--mobile Fz(14px) D(f) Ai(c) C($c-trend-down)")
low_height=soup.find("span",class_="Fw(600) Fz(16px)--mobile Fz(14px) D(f) Ai(c) C($c-trend-up)")

if low_low:
    print(low_low.text)
else:
    print(low_height.text)

#stock total qunatity
test=soup.find_all("span",class_="Fw(600) Fz(16px)--mobile Fz(14px)")
print(test[1].text)