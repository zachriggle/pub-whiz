#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
from beercommon import SearchForBeers, DumpBarToFixtures

beerNames = []
for line in file('snallygaster.txt'):
  beerNames.append(line)

results = SearchForBeers(beerNames)

DumpBarToFixtures("arundel.js", beerNames, {
  'id': 7,
  'name': "Snallygaster",
  'description': """Named for the fearsome and toothy mythical beast said to terrorize the region at the turn of the century,
Snallygaster returns once again to DC as a rollicking celebration of craft beer, ﬁne food, music and more.
For one day and one day only we'll simultaneously unleash more than 200 incomparable craft beers on the grounds
of Union Market DC against a backdrop featuring the area's top toques, the best of the best food trucks,
music, entertainment and family fun.""",
  'details': "",
  'url': "https://docs.google.com/file/d/0BxdmODFjEQHRcDNFTHIwQUNjcjg/edit?usp=sharing&pli=1",
  'map': "http://goo.gl/maps/vefQz",
})