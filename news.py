
#daily news
import requests
from bs4 import BeautifulSoup
headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
response=requests.get("https://tw.stock.yahoo.com/",headers=headers)
response2=requests.get("https://tw.stock.yahoo.com/quote/3714/news",headers=headers)
soup=BeautifulSoup(response.text,"html.parser")
soup2=BeautifulSoup(response2.text,"html.parser")

"""
daily_news=soup.find_all("a",class_="D(b) Td(n) Td(n):h C($c-link-text) C($c-active-text):h Fw(b) Fz(16px) Tov(e) Ov(h) Whs(nw)")
for news in daily_news:
    print("---------------------")
    print(news.text)
    print(news["href"])
    
    print("**********************")
#individual news
"""
indi_news=soup2.find_all("a",class_="Fw(b) Fz(20px) Fz(16px)--mobile Lh(23px) Lh(1.38)--mobile C($c-primary-text)! C($c-active-text)!:h LineClamp(2,46px)!--mobile LineClamp(2,46px)!--sm1024 mega-item-header-link Td(n) C(#0078ff):h C(#000) LineClamp(2,46px) LineClamp(2,38px)--sm1024 not-isInStreamVideoEnabled")
for indi in indi_news:
    print(indi.text)
    print(indi.get("href"))