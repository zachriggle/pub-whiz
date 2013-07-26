import urllib2
from bs4 import BeautifulSoup
from beercommon import SearchForBeers, DumpBarToFixtures

beersNamesUnicode = file('mash.txt').readlines()

beerNames         = beersNamesUnicode # [i.encode('utf-8') for i in beersNamesUnicode]

results = SearchForBeers(beerNames)

DumpBarToFixtures("mash.js", beerNames, {
  'id': 7,
  'name': "MGBMASH",
  'description': "", # "Max's Taphouse is Baltimore's premier beer pub. Max's is in the heart of historic Fells Point, just east of the Inner Harbor at Water Taxi Stop #11.",
  'details': "", # "With 140 rotating drafts, 5 Hand-Pumped Cask Ales, and  a world-spanning collection of approximately 1200 bottled beers in stock, Max's is legendary for having Maryland's largest selection of local and imported beer.",
  'url': "http://www.mgbmash.org",
  'map': "", #"http://goo.gl/maps/S0xDb",
})
