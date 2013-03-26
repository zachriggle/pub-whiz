import urllib2
from bs4 import BeautifulSoup
from beercommon import SearchForBeers, DisplayBeers

data = urllib2.urlopen("http://maxs.com").read()
soup = BeautifulSoup(data)

beersNamesUnicode = [i.contents[0]     for i in soup.find(id='p7tpc1_1').findAll('li')]
beerNames         = [i.encode('utf-8') for i in beersNamesUnicode]

results = SearchForBeers(beerNames)
DisplayBeers(beerNames)

# DumpBeersToFixtures("beer.js",  beerNames)
DumpBarToFixtures("maxs_taphouse.js", beerNames, {
  "name": "Maxs Taphouse",
  "description": "Max's Taphouse is Baltimore's premier beer pub. Max's is in the heart of historic Fells Point, just east of the Inner Harbor at Water Taxi Stop #11.",
  "url": "http://maxs.com",
  "beers": [beerData[name]["id"] for name in beerNames]
})