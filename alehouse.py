import urllib2
from bs4 import BeautifulSoup
from beercommon import SearchForBeers, DisplayBeers, DumpBarToFixtures

data = urllib2.urlopen("http://www.thealehousecolumbia.com/menu/").read()

# Dont care about bottles
data = data.split('<span>Bottles')[0]

soup = BeautifulSoup(data)

urlPattern   =r'http://beeradvocate.com/beer/profile/\d+/\d+(\?.*)?'
scorePattern =r'(?P<score>(\d+|N/A)) out of 100'
searchQuery  = ' "out of 100 based on" site:beeradvocate.com'

ales              = soup.find(id='ales').findAll('ul', 'col-post')
beersNamesUnicode = [i.find('span').contents[0] for i in ales]
beerNames         = [i.encode('utf-8') for i in beersNamesUnicode]

results = SearchForBeers(beerNames)
DisplayBeers(beerNames)

DumpBarToFixtures("alehouse.js", beerNames, {
  'id': 3,
  'name': "The Ale House",
  'description': "The Ale House Columbia is Howard County's destination for craft beers, food and nightlife. Come see what makes us more than the typical pub or sports bar.",
  'details': "",
  'url': "http://www.thealehousecolumbia.com",
  'map': "http://goo.gl/maps/IlqCL"
})