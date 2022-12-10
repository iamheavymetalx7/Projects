import pandas as pd 
import requests

from bs4 import BeautifulSoup

Product_Name=[]
Price=[]
Description =[]
Reviews = []

for i in range(2,10):


    url = "https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&page="+str(i)

    r =  requests.get(url)

    soup = BeautifulSoup(r.text,"lxml")
    box=soup.find("div", class_="_1YokD2 _3Mn1Gg")

    names = box.find_all("div", class_ = "_4rR01T")
    #print(names)

    for i in names:
        name = i.text
        Product_Name.append(name)


    # print(Product_Name)
    # print(len(Product_Name))


    prices =  box.find_all("div", class_="_30jeq3")



    for i in prices:
        name=i.text
        Price.append(name)
    #print(Price)


    desc = box.find_all("ul", class_="_1xgFaf")


    for i in desc:
        name=i.text
        Description.append(name)

    # print(Description)


    reviews = box.find_all("div",class_ = "_3LWZlK")

    for i in reviews:
        name=i.text
        Reviews.append(name)



# Now we will create a dataframe using pandas to get the item name, price, description and reviews.

df =pd.DataFrame({"Product Name": Product_Name, "Price":Price, "Description": Description, "Reviews": Reviews})

# print(df) 



df.to_csv('flipkart_mobiles_under_50K')