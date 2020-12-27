# These are to be integrated in the project
# Getting Links
import requests
import re
from bs4 import BeautifulSoup

url_input = input("Enter Your Question: ")
url = f"https://www.google.dz/search?q={url_input}"
page = requests.get(f"https://www.google.dz/search?q={url_input}")
soup = BeautifulSoup(page.content, "lxml")
for link in soup.find_all("a", href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
    links = re.split(":(?=http)", link["href"].replace("/url?q=", ""))
    print("----------------------------------------------------------------------------------------------------------------")
    print(links)

# ------------------------------------------------------------------------------------


# Getting Titles

r = requests.get(url)
content = r.content
soup = BeautifulSoup(content, "html.parser")
heading = soup.find_all("h3")
n = len(heading)
for x in range(n):
    titles = str.strip(heading[x].text)
    print("----------------------------------------------------------------------------------------------------------------")
    print(titles)
