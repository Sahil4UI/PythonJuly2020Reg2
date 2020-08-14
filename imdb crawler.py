import bs4
import urllib.request as url

movie = input("Enter Movie : ")

path = "https://www.imdb.com/find?q="+movie
response = url.urlopen(path)

page = bs4.BeautifulSoup(response , 'lxml')
td = page.find('td',class_="result_text")

a_tag = td.find('a')
a_href = a_tag['href']

newpath = "https://www.imdb.com"+a_href
response = url.urlopen(newpath)
moviePage = bs4.BeautifulSoup(response,'lxml')
div = moviePage.find("div",class_="title_wrapper")
name = div.find("h1")
name = name.text
print(name)

