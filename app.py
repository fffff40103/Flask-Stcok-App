from flask import Flask,render_template,request,redirect
import requests
from bs4 import BeautifulSoup

app=Flask(__name__)



headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}

@app.route("/")
def home_page():
    return render_template("homepage.html")

@app.route("/stock/<int:stock_number>")
def stock(stock_number):
    response=requests.get("https://tw.stock.yahoo.com/",headers=headers)
    response1=requests.get(f"https://tw.stock.yahoo.com/quote/{stock_number}",headers=headers)
    response2=requests.get(f"https://tw.stock.yahoo.com/quote/{stock_number}/news",headers=headers)
    soup=BeautifulSoup(response.text,"html.parser")
    soup1=BeautifulSoup(response1.text,"html.parser")
    soup2=BeautifulSoup(response2.text,"html.parser")
    # stock info like name and number
    store_data=[]
    store_price=[]
    store_indinews=[]
    store_dailynews=[]
    #every kind of stock price and total volume
    stock_name=soup1.find('h1',class_="C($c-link-text) Fw(b) Fz(24px) Mend(8px)").text
    stock_number=soup1.find('span',class_="C($c-icon) Fz(24px) Mend(20px)").text
    stock_deal=soup1.find("span",class_="Fw(600) Fz(16px)--mobile Fz(14px) D(f) Ai(c)").text
    open=soup1.find("span",class_="Fw(600) Fz(16px)--mobile Fz(14px) D(f) Ai(c)").text
    store_data.append(stock_name)
    store_data.append(stock_number)
    store_price.append(stock_deal)
    store_price.append(open)
    #heightest price
    height_up=soup1.find("span",class_="Fw(600) Fz(16px)--mobile Fz(14px) D(f) Ai(c) C($c-trend-up)")
    height_down=soup1.find("span",class_="Fw(600) Fz(16px)--mobile Fz(14px) D(f) Ai(c) C($c-trend-down)")
    if height_up:
        print(height_up.text)
        store_price.append(height_up.text)
    else:
        print(height_down.text)
        store_price.append(height_down.text)
    #lowest price
    low_low=soup1.find("span",class_="Fw(600) Fz(16px)--mobile Fz(14px) D(f) Ai(c) C($c-trend-down)")
    low_height=soup1.find("span",class_="Fw(600) Fz(16px)--mobile Fz(14px) D(f) Ai(c) C($c-trend-up)")

    if low_low:
        print(low_low.text)
        store_price.append(low_low.text)
    else:
        print(low_height.text)
        store_price.append(low_height.text)
    #stock total volumne
    test=soup1.find_all("span",class_="Fw(600) Fz(16px)--mobile Fz(14px)")
    print(test[1].text)
    store_price.append(test[1].text)
    #individual news
    indi_news=soup2.find_all("a",class_="Fw(b) Fz(20px) Fz(16px)--mobile Lh(23px) Lh(1.38)--mobile C($c-primary-text)! C($c-active-text)!:h LineClamp(2,46px)!--mobile LineClamp(2,46px)!--sm1024 mega-item-header-link Td(n) C(#0078ff):h C(#000) LineClamp(2,46px) LineClamp(2,38px)--sm1024 not-isInStreamVideoEnabled",limit=13)
    for indi in indi_news:
        store_indinews.append({indi.text:indi.get("href")})
    #daily news
    daily_news=soup.find_all("a",class_="D(b) Td(n) Td(n):h C($c-link-text) C($c-active-text):h Fw(b) Fz(16px) Tov(e) Ov(h) Whs(nw)",limit=13)
    for news in daily_news:
        store_dailynews.append({news.text:indi.get("href")}) 
    return render_template("stock.html",store_price=store_price,store_data=store_data,store_indinews=store_indinews,store_dailynews=store_dailynews)
    
    
    
@app.route("/",methods=["POST"])
def home_search():
    if request.method=="POST":
        searched_number=request.form["number"]
    return redirect(f'/stock/{searched_number}')

if __name__ == "__main__":
    app.run(port=5000, debug=True)