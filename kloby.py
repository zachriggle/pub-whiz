import urllib2
from bs4 import BeautifulSoup
from beercommon import SearchForBeers, DumpBarToFixtures

#
# VGP is stupid and paginates their beer
#


beersNamesUnicode = []

for page in [1,2,3]:
  url  = "http://victoriagastropub.com/?menutype=beer&paged=%s" % page
  data = urllib2.urlopen(url).read()
  soup = BeautifulSoup(data)

  beersNamesUnicode += soup.findAll('h2', 'menu-title')

beerNames = [
"Flying Dog - Single Hop Galaxy",
"Blue Mountain Brewery - Barrel Collection Mandolin",
"Duclaw - Naked Fish",
"New Belgium Brewing - Fat Tire",
"Fox Barrel - As You Wish Cider",
"Lefebvre - Hopus",
"Blue Mountain Brewery - Barrel Aged Dirty Belgian",
"Widmer Brothers Brewing - Nelson",
"Bud Light",
"Murphy's Irish Stout",
"DuClaw - Celtic Fury Irish Nitro",
"Murphy's - Irish Stout Nitro",
"Murphy's - Irish Red",
"Kilkenny - Irish Cream Ale",
"Harpoon - Celtic Red Ale",
"Guinness Stout",
"Widmer Brothers - O'ryely",
"Blue Point Brewing - No Apologies",
"Flying Dog - Lucky SOB",
"Devils Backbone - 8 Point",
"Devils Backbone - Vienna Lager",
"Devils Backbone - Reilly's Red Ale",
"Devils Backbone - Schwartz Bier",
"Devils Backbone - Kilt Flasher",
"Devils Backbone - Heavy Seas Big DIPA",
"Brooklyn Brewery - Black",
"Brooklyn Brewery - Sorachi Ace",
"Brooklyn Brewery - Bown Ale",
"Brooklyn Brewery - Brooklyn East IPA",
"Heavy Seas - Loose Cannon",
"Starr Hill - The Gift"
]

results = SearchForBeers(beerNames)

DumpBarToFixtures("kloby.js", beerNames, {
  'id': 5,
  'name': "Kloby's Smokehouse",
  'description': "",
  'deatils': "",
  'url': "http://www.klobysbbq.com/",
  'map': "http://goo.gl/maps/QJnV4",
})