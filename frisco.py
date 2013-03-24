import urllib2
from bs4 import BeautifulSoup
from beercommon import SearchForBeers, DisplayBeers

data = urllib2.urlopen("http://beer.friscogrille.com").read()
soup = BeautifulSoup(data)

urlPattern   =r'http://beeradvocate.com/beer/profile/\d+/\d+(\?.*)?'
scorePattern =r'(?P<score>(\d+|N/A)) out of 100'
searchQuery  = ' "out of 100 based on" site:beeradvocate.com'

beersNamesUnicode = [i.contents[0]     for i in soup.find('div', id='drafts').findAll('a')]
beerNames         = [i.encode('utf-8') for i in beersNamesUnicode]
beerNames.remove('Full Website')

results = SearchForBeers(beerNames)
DisplayBeers(beerNames)