from bs4 import BeautifulSoup
import requests
import csv

response=requests.get("https://www.rithmschool.com/blog")
soup= BeautifulSoup(response.text,"html.parser")
articles=soup.find_all("article")
with open("blogdata.csv","w",newline="") as csv_file:
  csv_writer=csv.DictWriter(csv_file,["title","url","date"])
  csv_writer.writeheader()
  for article in articles:
    a_tag= article.find("a")
    title=a_tag.get_text()
    url=a_tag["href"]
    date=article.find("time")["datetime"]
    csv_writer.writerow({"title":title,"url":url,"date":date})

    
    





