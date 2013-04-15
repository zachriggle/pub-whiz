import urllib2
from bs4 import BeautifulSoup
from beercommon import SearchForBeers, DumpBarToFixtures
import subprocess
import ocr
import tempfile
import os.path
import re

percent = '\d+\.?\d* *%'
quoteToEnd = '"[^"]+$'
alphaNumSpace = '[^A-Za-z0-9 ]'
lowerUpperLower = '([a-z])([A-Z])([a-z])'

url    = 'http://www.klobysbbq.com/beer-baltimore-best-bbq-ribs-barbebue-chicken-laurel-county-md.php'
data   = urllib2.urlopen(url).read()
soup   = BeautifulSoup(data)
images = [img.get('src') for img in soup.findAll('input')]
want   = None

#
# Kloby's website is pretty inconsistent
# 

for image in images:
  if 'BeerList' in image:
    want = image
  if 'BeerScreen' in image:
    want = image
  if 'Presentation' in image:
    want = image
  if 'BeerScreen' in image:
    want = image

if 'http' not in want:
  want = 'http://www.klobysbbq.com/' + want

imageData = urllib2.urlopen(want).read()
imgFile   = tempfile.mktemp(os.path.basename(want))

file(imgFile,'wb+').write(imageData)

ocrData = ocr.ocr(imgFile)

beerNames = []

for line in ocrData.split('\n'):

  if len(line.strip()) == 0:  continue
  if 'Today' in line:         continue

  line = re.sub(percent, "", line)
  line = re.sub(quoteToEnd, "", line)
  line = re.sub(alphaNumSpace, "", line)
  line = re.sub(lowerUpperLower, "\\1 \\2 \\3", line)
  beerNames.append(line)

results = SearchForBeers(beerNames)

DumpBarToFixtures("kloby.js", beerNames, {
  'id': 5,
  'name': "Kloby's Smokehouse",
  'description': "",
  'deatils': "",
  'url': "http://www.klobysbbq.com/",
  'map': "http://goo.gl/maps/QJnV4",
})