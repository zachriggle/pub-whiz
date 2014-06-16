import urllib2
from bs4 import BeautifulSoup
from beercommon import SearchForBeers, DumpBarToFixtures

url  = "http://www.duclaw.com/nowontap.aspx"
data = urllib2.urlopen(url).read()
soup = BeautifulSoup(data)

locations = soup.findAll('td', 'beerhead')

beersNamesUnicode = []

for loc in locations:
  try:
    locName = loc.find('a').contents[-1]
    if locName == 'Arundel Mills':
      barImages = loc.findAll('img')
      beersNamesUnicode = [i.get('alt') for i in barImages]
  except: pass

beerNames         = ['DuClaw ' + i.encode('utf-8') for i in beersNamesUnicode]

results = SearchForBeers(beerNames)

DumpBarToFixtures("arundel.js", beerNames, {
  'id': 7,
  'name': "DuClaw",
  'description': "The #1 craft brewery in Maryland (ratebeer.com), DuClaw Brewing Company offers award winning handcrafted beers with tastes and flavors as provocative as their names.",
  'details': "",
  'url': "http://www.duclaw.com",
  'map': "http://goo.gl/maps/gMS7W",
})