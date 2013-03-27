import urllib2
import json
import re
import os
import sys
import pprint
import HTMLParser
import multiprocessing
from bs4 import BeautifulSoup

from cache import beers as beerData

baUrlPattern   =r'http://beeradvocate.com/beer/profile/\d+/\d+(\?.*)?'
baScorePattern =r'(?P<score>(\d+|N/A)) out of 100'
baQuery      = ' "out of 100 based on" site:beeradvocate.com'

rbQuery      = ' site:ratebeer.com'
rbStylePattern = r'!Style: !(?P<style>[^!]+)'
rbAbvPattern   = r'!ABV!: !(?P<abv>[\.\d]+%)!'
rbDescPattern  = r'!COMMERCIAL DESCRIPTION!(?P<description>[^!]+)'
rbScorePattern = r'(?P<score>\d+) at RateBeer!'
rbAliasPattern = r'Proceed to the aliased beer...<br><br><A HREF="(?P<url>[^"]+)'

def unescape(text):
    return unicode(BeautifulSoup(text))

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

def SearchForBeer(beer):
    # cached?
    if beer in beerData: 
        return beerData[beer]

    print beer

    data = { 
        'name': beer,
        'result': '', 
        'baUrl': "http://google.com/?q=%s" % beer,
        'rbUrl': "http://google.com/?q=%s" % beer,
        'baScore': '??',
        'rbScore': '??',
        'style': "",
        'abv': "",
        'description': ""
    }

    #
    # Search for BeerAdvocate
    #
    results = search(beer + baQuery)
    
    for result in results:

        # only care about results that look like:
        # beeradvocate.com/beer/profile/15237/58905
        if not re.match(baUrlPattern, result['Url']):
            continue

        description = result['Description']
        matches     = re.search(baScorePattern, description)
        if matches:
            data['result'] = result
            data['baScore']  = matches.group('score')
            data['baUrl']  = result['Url']
            break # Stop after the first (best) result

    #
    # Search for RateBeer
    #
    results = search(beer + rbQuery)

    if len(results):
        r = results[0]

        data['rbUrl'] = r['Url']

        #
        # Parse the RateBeer page for ABV and Style
        #
        html = urllib2.urlopen(r['Url']).read()

        #  Aliased beer?
        alias = re.search(rbAliasPattern,html)
        if alias:
            html = urllib2.urlopen('http://ratebeer.com/' + alias.group('url')).read()

        text = BeautifulSoup(html).get_text('!').encode('utf-8')

        try:    data['rbScore'] = re.search(rbScorePattern, text).group('score')
        except: pass

        try:    data['style'] = unescape(re.search(rbStylePattern, text).group('style'))
        except: pass

        try: data['abv']   = re.search(rbAbvPattern, text).group('abv')
        except: pass     

        try:    data['description'] = unescape(re.search(rbDescPattern, text).group('description'))
        except: pass

    if data['baScore'] == 'N/A':
        data['baScore'] = '??'

    return data

def SearchForBeers(beerNames):
    global beerData
    pool = multiprocessing.Pool()

    results = pool.map(SearchForBeer, beerNames)

    for result in results:
        if result['name'] not in beerData.keys():
            result['id'] =  1 + len(beerData)
            beerData[result['name']] = result

    file('cache.py','w+').write('beers = %s\n' % pprint.pformat(beerData))


def DumpBeerToFixtures():
    global beerData

    beers = []

    for k,v in beerData.items():

        data = dict(v)
        del data['result']
        beers.append(data)

    file('beer.js','w+').write("""
App.Beer.FIXTURES = %s
""" % json.dumps(beers))

def DumpBarToFixtures(filename, beerNames, barData):
    global beerData

    for k,v in beerData.items():
        print k
        print "%d %s" % (v['id'], k)

    barData['beers'] = [beerData[name]["id"] for name in beerNames]

    file(filename,'w+').write("""
$(function () {
App.Bar.FIXTURES.push(%s);
})
""" % json.dumps(barData))

    DumpBeerToFixtures()
