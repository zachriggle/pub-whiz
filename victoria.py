import urllib2
from bs4 import BeautifulSoup
from beercommon import SearchForBeers, DumpBarToFixtures

#
# VGP is stupid and paginates their beer
#


beersNamesUnicode = []

for page in [1,2,3]:
  url  = "http://victoriagastropub.com/?menutype=beer&paged=%s" % page
  data = urllib2.urlopen(url, timeout=15).read() or ""
  soup = BeautifulSoup(data)

  beersNamesUnicode += soup.findAll('h4', 'menu-title')

beerNames = [i.contents[1].encode('utf-8') for i in beersNamesUnicode]

results = SearchForBeers(beerNames)

DumpBarToFixtures("victoria.js", beerNames, {
  'id': 4,
  'name': "Victoria Gastropub",
  'description': "Restaurant and bar serving modern British fare, brunch, lunch & dinner with wide selection of draft beers. Late night menu and private dining.",
  'deatils': "A place with a warm, inviting atmosphere that serves sophisticated & innovative creations on classic pub fare with an eclectic beer & wine list.",
  'url': "http://www.victoriagastropub.com",
  'map': "http://goo.gl/maps/0Ysem",
})