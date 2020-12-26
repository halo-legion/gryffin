import requests
import re
from bs4 import BeautifulSoup

url_input = input("Enter Your Question: ")
# Getting Links

page = requests.get(f"https://www.google.dz/search?q={url_input}")
soup = BeautifulSoup(page.content, "lxml")
links = soup.findAll("a")
for link in soup.find_all("a", href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
  print(re.split(":(?=http)", link["href"].replace("/url?q=","")))

#------------------------------------------------------------------------------------


