import re
import json
from bs4 import BeautifulSoup
import urllib2
import urllib
import os
import sys
import pdb

def get_each_list(site):
    html = urllib2.urlopen(site).read()
    soup = BeautifulSoup(html)
    pois = soup.find_all('ul',{'class':'clearfix', 'data-tagid':'0'})[0]
    poi_elements = pois.find_all('a')
    for poi in poi_elements:
        poiname = poi.contents[0].contents[0].encode('utf8')
        url = 'http://www.mafengwo.cn' + poi.attrs['href']
        print '\t'.join([poiname, url])

def get_all_pois(site):
    html = urllib2.urlopen(site).read()
    soup = BeautifulSoup(html)
    l = soup.find_all('dd') + soup.find_all('dt')
    for line in l:
        line_elems = line.find_all('a')
        for elem in line_elems:
            poi_id = elem.attrs['href'].split('/')[-1][0:-5]
            try:
                poi_name = elem.contents[0].encode('utf8')
                print 'ADDR:', poi_name
                url = 'http://www.mafengwo.cn/jd/' + poi_id + '/gonglve.html'
                get_each_list(url)
            except:
                print >> sys.stderr, 'ERROR in crawling', poi_name
                pass

if __name__ == '__main__':
    get_all_pois('http://www.mafengwo.cn/mdd/')
