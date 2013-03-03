import cache
import json
import re
import pprint
import urllib2
from bs4 import BeautifulSoup

data = urllib2.urlopen("http://maxs.com").read()
soup = BeautifulSoup(data)

urlPattern   =r'http://beeradvocate.com/beer/profile/\d+/\d+(\?.*)?'
scorePattern =r'(?P<score>(\d+|N/A)) out of 100'
searchQuery  = ' "out of 100 based on" site:beeradvocate.com'

beersNamesUnicode = [i.contents[0]     for i in soup.find(id='p7tpc1_1').findAll('li')]
beerNames         = [i.encode('utf-8') for i in beersNamesUnicode]
beerData          = cache.beers

def search(query):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)'
    key        = 'uPEdkg+ybWk/vZjHh7EX+WH3NAFoPaDuvr4WD9VgJDs='
    creds      = (':%s' % key).encode('base64')[:-1]
    auth       = 'Basic %s' % creds
    
    query      = urllib2.quote("'%s'" % query)
    request    = urllib2.Request('https://api.datamarket.azure.com/Bing/SearchWeb/v1/Web?Query=%s&$top=5&$format=json' % query)

    request.add_header('Authorization', auth)
    request.add_header('User-Agent', user_agent)
    
    requestor = urllib2.build_opener()
    result    = requestor.open(request) 
    data      = result.read()

    return json.loads(data)['d']['results']

for beer in beerNames:
    # cached?
    if beer in beerData: 
        continue

    results = search(beer + searchQuery)
    data = { 'score': 0, 'result': '' }
    
    for result in results:

        # only care about results that look like:
        # beeradvocate.com/beer/profile/15237/58905
        if not re.match(urlPattern, result['Url']):
            continue

        description = result['Description']
        matches     = re.search(scorePattern, description)
        if matches:
            data['result'] = result
            data['score'] = matches.group('score')
            break # Stop after the first (best) result

    beerData[beer] = data

def getScore((a,b)):
    try:    return int(b['score']) # 0 # return data['score']
    except: return -1

for name,data in sorted(beerData.items(), key=getScore, reverse=True):
    print "%3s " % data['score'],
    print name


# pprint.pprint(beerData)

# write data to disk for next time
file('cache.py','w+').write('beers = %s\n' % pprint.pformat(beerData))