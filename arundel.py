import urllib2
from bs4 import BeautifulSoup
from beercommon import SearchForBeers, DumpBarToFixtures
import re
import codecs

url  = "http://www.duclaw.com/wp-content/themes/duclaw/loopHandler_OnTap.php?numPosts=100&pageNumber=1&catID=0&taxTerm=location-arundel-mills"
data = urllib2.urlopen(url).read()
soup = BeautifulSoup(data)
pat  = r'.*/beer/(.*)/'

links = [link.get('href') for link in soup.findAll('a')]



def ProcessLink(link):
  url      = link.get('href')
  beerName = re.search(pat, url).group(1)
  return codecs.encode('DuClaw ' + beerName.replace('-', ' '), 'utf-8')

beerNames = map(ProcessLink, soup.findAll('a'))
print beerNames
results = SearchForBeers(beerNames)

DumpBarToFixtures("arundel.js", beerNames, {
  'id': 7,
  'name': "DuClaw",
  'description': "The #1 craft brewery in Maryland (ratebeer.com), DuClaw Brewing Company offers award winning handcrafted beers with tastes and flavors as provocative as their names.",
  'details': "",
  'url': "http://www.duclaw.com",
  'map': "http://goo.gl/maps/gMS7W",
})