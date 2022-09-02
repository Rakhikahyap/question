import requests
from bs4 import BeautifulSoup
url_req=requests.get("https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in")
print(url_req)
Soup=BeautifulSoup(url_req.content,"html.parser")
# print(Soup)
movie_data=Soup.find("div",class_="lister")
# print(movie_data)
list=[]
for i in movie_data:
# print(i)

