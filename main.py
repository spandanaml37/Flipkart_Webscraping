import pandas as pd
import requests
from bs4 import BeautifulSoup
from pandas import DataFrame
product_name = []
prices = []
description = []
reviews =[]
for i in range(2,12):
    url = "https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&page="+str(i)

    r=requests.get(url)
    #print(r)

    soup = BeautifulSoup(r.text,"lxml")
    box = soup.find("div",class_="_1YokD2 _3Mn1Gg")
    #print(soup)
    #while True:
    # np=soup.find("a",class_ ="_1LKTO3").get("href")
    #cnp="https://www.flipkart.com/"+np
    #print(cnp)

        #url =cnp
        #r=requests.get(url)
        #soup=BeautifulSoup(r.text,"lxml")
    names=box.findAll("div",class_="_4rR01T")
    #print(names)
    for i in names:
        name=i.text
        product_name.append(name)

    #print(product_name)

    pro_price = box.findAll("div",class_="_30jeq3 _1_WHN1")
    #print(prices)

    for i in pro_price:
        price=i.text
        prices.append(price)
    #print(prices)


    desc=box.findAll("ul",class_="_1xgFaf")

    for i in desc:
        descr=i.text
        description.append(descr)
    #print(description)

    review = box.findAll("div",class_="_3LWZlK")
    for i in review:
        re=i.text
        reviews.append(re)

    #print(len(reviews))
print(len(product_name))
print(len(prices))
print(len(description))
print(len(reviews))

df = pd.DataFrame({"Product name":product_name,"Prices":prices,"Description":description})
#print(df)
df = pd.DataFrame({"Product name":product_name,"Prices":prices,"Description":description,"Reviews":reviews}) #This line can be used when size of all the inputs are same

df.to_csv("D:/WebScarping/flipkart_mobiles.csv")

df1 = pd.DataFrame({"Reviews":reviews})

df1.to_csv("D:/WebScarping/flipkart_mobiles_reviews.csv")



