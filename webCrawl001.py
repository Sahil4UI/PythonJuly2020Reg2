import bs4
import urllib.request as url1

path = "https://www.amazon.in/Apple-iPhone-11-64GB-White/dp/B07XVMCLP7/ref=sr_1_5?dchild=1&keywords=iphone+11&qid=1597308263&sr=8-5"

#1 -> send request
response = url1.urlopen(path)

#print(response)

data = bs4.BeautifulSoup(response,'lxml')

productName = data.find("span",id="productTitle")

#print(type(productName.text))

productName = productName.text.strip()

print("Product Name : ",productName)

mrp=data.find('span',id="priceblock_ourprice")

print("MRP : ",mrp.text)


