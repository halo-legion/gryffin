import re
import requests

from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect
from django.shortcuts import render

best_websites_data = ['https://analytics.moz.com', 'https://youcandothecube.com', 'https://www.wikihow.com',
                      'https://www.wired.com', 'https://www.samsung.com', 'https://www.reddit.com',
                      'https://www.quora.com', 'https://www.facebook.com', 'https://brainly.in',
                      'https://katmoviehd.se', 'https://www.toppr.com', 'https://learn', 'https://www.apple.com',
                      'https://www.youtube.com', 'https://www.blogger.com', 'https://www.microsoft.com',
                      'https://www.cloudflare.com', 'https://play.google.com', 'https://docs.google.com',
                      'https://en.wikipedia.org', 'https://linkedin.com', 'https://maps.google.com',
                      'https://mozilla.org', 'https://www.adobe.com', 'https://wordpress.org', 'https://europa.eu',
                      'https://drive.google.com', 'https://vimeo.com', 'https://sites.google.com', 'https://vk.com',
                      'https://istockphoto.com', 'https://facebook.com', 'https://cnn.com', 'https://line.me',
                      'https://bp.blogspot.com', 'https://amazon.com', 'https://uol.com.br', 'https://bbc.co.uk',
                      'https://es.wikipedia.org', 'https://github.com', 'https://pt.wikipedia.org',
                      'https://gstatic.com', 'https://google.es', 'https://opera.com', 'https://fr.wikipedia.org',
                      'https://nih.gov', 'https://paypal.com', 'https://forbes.com', 'https://nytimes.com',
                      'https://creativecommons.org', 'https://live.com', 'https://whatsapp.com', 'https://dropbox.com',
                      'https://t.me', 'https://google.com.br', 'https://news.yahoo.com', 'https://mail.google.com',
                      'https://theguardian.com', 'https://wikimedia.org', 'https://jimdofree.com',
                      'https://hugedomains.com', 'https://dailymotion.com', 'https://news.google.com',
                      'https://medium.com', 'https://www.yahoo.com', 'https://slideshare.net',
                      'https://policies.google.com', 'https://google.de', 'https://issuu.com', 'https://bbc.com',
                      'https://myspace.com', 'https://www.imdb.com', 'https://w3.org', 'https://washingtonpost.com',
                      'https://get.google.com', 'https://mail.ru', 'https://msn.com', 'https://feedburner.com',
                      'https://reuters.com', 'https://google.co.jp', 'https://globo.com',
                      'https://developers.google.com', 'https://abril.com.br', 'https://harvard.edu',
                      'https://booking.com', 'https://wsj.com', 'https://google.ru', 'https://search.google.com',
                      'https://pinterest.com', 'https://telegraph.co.uk', 'https://aboutads.info',
                      'https://dailymail.co.uk', 'https://cpanel.net', 'https://goo.gl', 'https://mirror.co.uk',
                      'https://bloomberg.com', 'https://hatena.ne.jp', 'https://foxnews.com',
                      'https://books.google.com', 'https://ok.ru', 'https://wikia.com', 'https://twitter.com',
                      'https://ig.com.br', 'https://time.com', 'https://elpais.com', 'https://amazon.co.jp',
                      'https://scribd.com', 'https://themeforest.net', 'https://picasaweb.google.com',
                      'https://telegram.me', 'https://independent.co.uk', 'https://plesk.com',
                      'https://marketingplatform.google.com', 'https://thesun.co.uk', 'https://nasa.gov',
                      'https://google.co.uk', 'https://un.org', 'https://abcnews.go.com',
                      'https://translate.google.com', 'https://tinyurl.com', 'https://google.it', 'https://www.gov.uk',
                      'https://aol.com', 'https://it.wikipedia.org', 'https://aliexpress.com',
                      'https://huffingtonpost.com', 'https://ft.com', 'https://cdc.gov', 'https://who.int',
                      'https://cpanel.com', 'https://dan.com', 'https://photos.google.com', 'https://namecheap.com',
                      'https://change.org', 'https://businessinsider.com', 'https://www.amazon.co.uk',
                      'https://gravatar.com', 'https://buydomains.com', 'https://id.wikipedia.org',
                      'https://lefigaro.fr', 'https://tools.google.com', 'https://networkadvertising.org',
                      'https://wired.com', 'https://android.com', 'https://rakuten.co.jp',
                      'https://files.wordpress.com', 'https://youronlinechoices.com', 'https://bit.ly',
                      'https://office.com', 'https://google.fr', 'https://cnet.com', 'https://mediafire.com',
                      'https://draft.blogger.com', 'https://bing.com', 'https://archive.org',
                      'https://steampowered.com', 'https://latimes.com', 'https://usatoday.com', 'https://fb.com',
                      'https://4shared.com', 'https://fandom.com', 'https://www.wix.com', 'https://ebay.com',
                      'https://de.wikipedia.org', 'https://samsung.com', 'https://terra.com.br',
                      'https://www.amazon.de', 'https://webmd.com', 'https://ja.wikipedia.org', 'https://xbox.com',
                      'https://bandcamp.com', 'https://theglobeandmail.com', 'https://urbandictionary.com',
                      'https://nbcnews.com', 'https://godaddy.com', 'https://vice.com', 'https://express.co.uk',
                      'https://skype.com', 'https://welt.de', 'https://berkeley.edu', 'https://sapo.pt',
                      'https://www.weebly.com', 'https://bloglovin.com', 'https://sendspace.com',
                      'https://netvibes.com', 'https://e-recht24.de', 'https://m.wikipedia.org', 'https://cnbc.com',
                      'https://cornell.edu', 'https://instructables.com', 'https://my.yahoo.com', 'https://detik.com',
                      'https://huffpost.com', 'https://enable-javascript.com', 'https://ovh.co.uk',
                      'https://pl.wikipedia.org', 'https://lemonde.fr', 'https://nature.com', 'https://gofundme.com',
                      'https://rapidshare.com', 'https://depositfiles.com', 'https://surveymonkey.com',
                      'https://walmart.com', 'https://spotify.com', 'https://imageshack.us', 'https://ign.com',
                      'https://nokia.com', 'https://economist.com', 'https://groups.google.com', 'https://spiegel.de',
                      'https://afternic.com', 'https://google.nl', 'https://ytimg.com', 'https://cbc.ca',
                      'https://metro.co.uk', 'https://ovh.net', 'https://newsweek.com', 'https://theatlantic.com',
                      'https://abc.es', 'https://wp.com', 'https://ipv4.google.com', 'https://abc.net.au',
                      'https://disney.com', 'https://columbia.edu', 'https://eventbrite.com', 'https://rt.com',
                      'https://ibm.com', 'https://dell.com', 'https://kickstarter.com', 'https://worldbank.org',
                      'https://stackoverflow.com', 'https://smh.com.au', 'https://naver.jp',
                      'https://nationalgeographic.com', 'https://goodreads.com', 'https://yale.edu', 'https://ovh.com',
                      'https://cnil.fr', 'https://umich.edu', 'https://wikihow.com', 'https://news.com.au',
                      'https://finance.yahoo.com', 'https://unesco.org', 'https://google.co.in', 'https://stanford.edu',
                      'https://asus.com', 'https://bp2.blogger.com', 'https://000webhost.com',
                      'https://shutterstock.com', 'https://npr.org', 'https://rambler.ru', 'https://washington.edu',
                      'https://nikkei.com', 'https://nicovideo.jp', 'https://bt.com', 'https://disqus.com',
                      'https://oup.com', 'https://discord.gg', 'https://loc.gov', 'https://icann.org',
                      'https://psychologytoday.com', 'https://chicagotribune.com', 'https://php.net',
                      'https://elmundo.es', 'https://noaa.gov', 'https://ziddu.com', 'https://www.amazon.fr',
                      'https://sedo.com', 'https://apache.org', 'https://theverge.com', 'https://allaboutcookies.org',
                      'https://mozilla.com', 'https://akamaihd.net', 'https://nginx.com', 'https://privacyshield.gov',
                      'https://cambridge.org', 'https://deezer.com', 'https://nypost.com', 'https://twitch.tv',
                      'https://blackberry.com', 'https://espn.com', 'https://about.com', 'https://target.com',
                      'https://hm.com', 'https://greenpeace.org', 'https://forms.gle', 'https://ea.com',
                      'https://newyorker.com', 'https://nydailynews.com', 'https://sfgate.com', 'https://ox.ac.uk',
                      'https://search.yahoo.com', 'https://yelp.com', 'https://goo.ne.jp', 'https://ggpht.com',
                      'https://www.amazon.es', 'https://doubleclick.net', 'https://weibo.com', 'https://addthis.com',
                      'https://princeton.edu', 'https://yahoo.co.jp', 'https://gizmodo.com', 'https://ikea.com',
                      'https://nvidia.com', 'https://britannica.com', 'https://ietf.org', 'https://academia.edu',
                      'https://naver.com', 'https://buzzfeed.com', 'https://playstation.com', 'https://gmail.com',
                      'https://alibaba.com', 'https://google.co.id', 'https://quora.com', 'https://digg.com',
                      'https://pixabay.com', 'https://sputniknews.com', 'https://mysql.com', 'https://ru.wikipedia.org',
                      'https://nginx.org', 'https://engadget.com', 'https://www.wikipedia.org', 'https://mega.nz',
                      'https://google.pl', 'https://usnews.com', 'https://tripadvisor.com', 'https://shopify.com',
                      'https://variety.com', 'https://ted.com', 'https://oracle.com', 'https://wiley.com',
                      'https://techcrunch.com', 'https://hollywoodreporter.com', 'https://whitehouse.gov',
                      'https://list-manage.com', 'https://sciencedirect.com', 'https://standard.co.uk',
                      'https://hp.com', 'https://storage.googleapis.com', 'https://yandex.ru',
                      'https://secureserver.net', 'https://scoop.it', 'https://thetimes.co.uk', 'https://google.com.tw',
                      'https://photobucket.com', 'https://www.over-blog.com', 'https://netflix.com',
                      'https://soundcloud.com', 'https://box.com', 'https://googleblog.com', 'https://instagram.com',
                      'https://yadi.sk', 'https://wa.me', 'https://sciencemag.org', 'https://researchgate.net',
                      'https://guardian.co.uk', 'https://picasa.google.com', 'https://channel4.com',
                      'https://mashable.com', 'https://over-blog-kiwi.com', 'https://sciencedaily.com',
                      'https://biglobe.ne.jp', 'https://ria.ru', 'https://zendesk.com', 'https://dw.com',
                      'https://cbsnews.com', 'https://code.google.com', 'https://trustpilot.com',
                      'https://addtoany.com', 'https://pbs.org', 'https://bitly.com', 'https://mit.edu',
                      'https://google.ca', 'https://indiatimes.com', 'https://gnu.org', 'https://t.co',
                      'https://prestashop.com', 'https://iubenda.com', 'https://ebay.co.uk', 'https://imageshack.com',
                      'https://sina.com.cn', 'https://kinja.com', 'https://m.me', 'https://utexas.edu',
                      'https://woocommerce.com', 'https://nps.gov', 'https://megaupload.com',
                      'https://photos1.blogger.com', 'https://home.pl', 'https://csmonitor.com', 'https://ameblo.jp',
                      'https://calameo.com', 'https://lifehacker.com', 'https://people.com', 'https://stores.jp',
                      'https://zoom.us', 'https://www.canalblog.com', 'https://inc.com', 'https://iso.org',
                      'https://dribbble.com', 'https://nifty.com', 'https://digitaltrends.com', 'https://redhat.com',
                      'https://nhk.or.jp', 'https://rollingstone.com', 'https://w3schools.com',
                      'https://livescience.com', 'https://dreniq.com', 'https://wiktionary.org', 'https://lycos.com',
                      'https://fb.me', 'https://liveinternet.ru', 'https://irs.gov', 'https://epa.gov',
                      'https://qq.com', 'https://www.livejournal.com', 'https://xinhuanet.com',
                      'https://thenextweb.com', 'https://symantec.com', 'https://arxiv.org', 'https://viagens.com.br',
                      'https://thoughtco.com', 'https://consumerreports.org', 'https://ca.gov', 'https://offset.com',
                      'https://statista.com', 'https://billboard.com', 'https://state.gov', 'https://politico.com',
                      'https://pinterest.co.uk', 'https://allrecipes.com', 'https://20minutos.es', 'https://udemy.com',
                      'https://cam.ac.uk', 'https://soratemplates.com', 'https://snapchat.com',
                      'https://thedailybeast.com', 'https://example.com', 'https://springer.com',
                      'https://brandbucket.com', 'https://tmz.com', 'https://adweek.com', 'https://ucla.edu',
                      'https://vox.com', 'https://evernote.com', 'https://www.amazon.com', 'https://ndtv.com',
                      'https://usgs.gov', 'https://feedburner.google.com', 'https://ucoz.ru',
                      'https://steamcommunity.com', 'https://www.amazon.ca', 'https://techradar.com',
                      'https://about.me', 'https://bund.de', 'https://merriam-webster.com', 'https://ap.org',
                      'https://mixcloud.com', 'https://prezi.com', 'https://fifa.com', 'https://blog.fc2.com',
                      'https://xing.com', 'https://ehow.com', 'https://coursera.org', 'https://fda.gov',
                      'https://ieee.org', 'https://mystrikingly.com', 'https://qz.com', 'https://fortune.com',
                      'https://eonline.com', 'https://ed.gov', 'https://chron.com', 'https://cisco.com',
                      'https://searchenginejournal.com', 'https://pcmag.com', 'https://bp1.blogger.com',
                      'https://khanacademy.org', 'https://video.google.com', 'https://behance.net', 'https://cmu.edu',
                      'https://plos.org', 'https://storage.canalblog.com', 'https://si.edu', 'https://asahi.com',
                      'https://google.com.au', 'https://eff.org', 'https://businesswire.com', 'https://home.neustar',
                      'https://autodesk.com', 'https://entrepreneur.com', 'https://chinadaily.com.cn',
                      'https://pastebin.com', 'https://debian.org', 'https://teamviewer.com', 'https://arstechnica.com',
                      'https://disney.go.com', 'https://huawei.com', 'https://repubblica.it', 'https://archives.gov',
                      'https://mayoclinic.org', 'https://mail.yahoo.com', 'https://zdnet.com', 'https://tes.com',
                      'https://newscientist.com', 'https://moz.com', 'https://scoopwhoop.com', 'https://programiz.com',
                      'https://www.algoexpert.io', 'https://flipkart.com', 'https://gktoday.in',
                      'https://thesaurus.com', 'https://geeksforgeeks.org', 'https://jagranjosh.com',
                      'https://halolegion.com', 'https://ncert.nic.in', 'https://images.google.com',
                      'https://primevideo.com', 'https://byjus.com', 'https://w3resource.com', 'https://ruwix.com',
                      'https://www.rubiks.com', 'https://www.youcandothecube.com']
link_raw = []
link_filter = []
best_link = []


def Home(request):
    query = request.POST.get('query')
    if request.method == 'POST':
        link_raw.clear()
        link_filter.clear()
        best_link.clear()
        bing = requests.get(f"https://www.bing.com/search?q={query}")
        google = requests.get(f"https://www.google.dz/search?q={query}")
        yahoo = requests.get(f"https://in.search.yahoo.com/search?p={query}")
        soup_google = BeautifulSoup(google.content, "lxml")
        soup_bing = BeautifulSoup(bing.content, "lxml")
        soup_yahoo = BeautifulSoup(yahoo.content, "lxml")
        for google_link in soup_google.find_all("a", href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
            google_links = re.split(":(?=http)", google_link["href"].replace("/url?q=", ""))
            link_raw.append(google_links)
        for bing_link in soup_bing.find_all("a", href=re.compile("(htt.*://.*)")):
            link_raw.append(bing_link["href"])
        for yahoo_link in soup_yahoo.find_all("a", href=re.compile("(htt.*://.*)")):
            link_raw.append(yahoo_link["href"])
        for link in link_raw:
            f0 = str(link)
            filter1 = re.sub(r'\[\'', '', f0)
            filter2 = re.sub(r'\'\]', '', filter1)
            filtered_links = str(filter2)
            link_filter.append(filtered_links)
        for new_link in link_filter:
            pattern = re.compile(r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b')
            matches = pattern.finditer(new_link)
            for match in matches:
                websites_name = match.group()
                for website_data in best_websites_data:
                    if website_data == websites_name and requests.get(new_link).status_code == 200 and new_link not in best_link:
                        best_link.append(new_link)
        if len(best_link) > 0:
            request.session['best_link'] = best_link
            return HttpResponseRedirect("https://gryffin-search-engine.herokuapp.com/results/")
        else:
            return render(request, "home.html", {"context": "No Results Found"})
    return render(request, "home.html")


def Results(request):
    return render(request, "results.html")


def error_404_views(request, exception):
    return render(request, "404.html")
