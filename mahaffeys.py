#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
from beercommon import SearchForBeers, DumpBarToFixtures
import re

beersNamesUnicode = []

url = "http://www.mahaffeyspub.com/beer/beers_in_stock.php"
data = urllib2.urlopen(url).read()
text = BeautifulSoup(data).get_text('!').encode('utf-8')

beerNamesUnicode = re.findall(r'\(D\) *([^\r\n]+)',text)

beerNames = [i.encode('utf-8') for i in beerNamesUnicode]

results = SearchForBeers(beerNames)

DumpBarToFixtures("mahaffeys.js", beerNames, {
  'id': 6,
  'name': "Mahaffey's",
  'description': "Canton's Best Beer Bar",
  'deatils': u"Located in historic Canton, Mahaffey’s is one of Baltimore’s finest beer bars. Featuring taps that rotate every day, a large selection of import and micro bottles, and a cask-conditioned beer on the hand pump, Mahaffey’s serves up a selection that can’t be beat. So come by for a drink, join the 100 Beer Club, say hello to Wayne (owner, proprietor and resident beer expert) and check out the excellent dinner menu while you’re here.",
  'url': "www.mahaffeyspub.com",
  'map': "http://goo.gl/maps/6xJuk",
})