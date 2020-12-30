from django.shortcuts import render
from django.http import HttpResponseRedirect
import requests
import re
from bs4 import BeautifulSoup

link_raw = []
def Home(request):
    query = request.POST.get('query')
    if request.method == 'POST':
        link_raw.clear()
        # bing = requests.get(f"https://www.bing.com/search?q={query}")
        # google = requests.get(f"https://www.google.dz/search?q={query}")
        yahoo = requests.get(f"https://in.search.yahoo.com/search?p={query}")
        # soup_google = BeautifulSoup(google.content, "lxml")
        # soup_bing = BeautifulSoup(bing.content, "lxml")
        soup_yahoo = BeautifulSoup(yahoo.content, "lxml")
        # for google_link in soup_google.find_all("a", href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
        #     google_links = re.split(":(?=http)", google_link["href"].replace("/url?q=", ""))
        #     link_raw.append(google_links)
        # for bing_link in soup_bing.find_all("a", href=re.compile("(htt.*://.*)")):
        #     link_raw.append(bing_link["href"])
        for yahoo_link in soup_yahoo.find_all("a", href=re.compile("(htt.*://.*)")):
            link_raw.append(yahoo_link["href"])
        return render(request, "results.html", {"context": link_raw})

    return render(request, "home.html")




def Results(request):
    return render(request, "results.html", {"context": link_raw})


