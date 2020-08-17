import bs4
import urllib.request as url
path="https://edition.cnn.com"
httprequest=url.urlopen(path)
page1=bs4.BeautifulSoup(httprequest, 'lxml')
a = page1.findAll('a',class_="sc-jzJRlG sc-kgoBCf fqbFTu")
print(a)

sportsintent = ['sports','sports news','tell me sports news','whats the Sports news']
Entertainment_intent = ['entertainment','entertainment news','tell me entertainment news','whats the entertainment news']
Business_intent = ['business','business news','tell me Business news','whats the entertainment news']
Health_intent = ['health','health news','tell me health news','whats the health news']


news = True
while news:
    choice = input("enter news category")
    if choice in sportsintent:
        Url = path + a[-2]['href']
        print("Sports headlines are as follows:")
        
        httprequest=url.urlopen(Url)
        page2=bs4.BeautifulSoup(httprequest, 'lxml')
        sportsnews = page2.findAll('span',class_='cd__headline-text')
        for i in range(10):
            news=sportsnews[i]
            print(i+1,news.text)
        print("****************************************")

    elif choice in Business_intent:
        Url = path + a[2]['href']
        print("Business headlines are as follows:")
        
        httprequest=url.urlopen(Url)
        page2=bs4.BeautifulSoup(httprequest, 'lxml')
        Businessnews = page2.findAll('span',class_='cd__headline-text')
        for i in range(10):
            news=Businessnews[i]
            print(i+1,news.text)
        print("****************************************")


        
    elif choice in Entertainment_intent:
         Url = path + a[4]['href']
         print("Entertainment headlines are as follows:")
         httprequest=url.urlopen(Url)
         page3=bs4.BeautifulSoup(httprequest, 'lxml')
         entertainmentnews = page3.findAll('span',class_='cd__headline-text')
         for i in range(10):
              news=entertainmentnews[i]
              print(i+1,news.text)
         print("****************************************")

    elif choice in Health_intent:
         Url = path + a[3]['href']
         
         print("health headlines are as follows:")
         httprequest=url.urlopen(Url)
         page4=bs4.BeautifulSoup(httprequest, 'lxml')
         healthnews = page4.findAll('span',class_='cd__headline-text')
         for i in range(10):
              news=healthnews[i]
              print(i+1,news.text)
         print("****************************************")

    else:
        print("Invalid Category")
        news = False
