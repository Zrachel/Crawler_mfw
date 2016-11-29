import urllib2
import json
import time
from bs4 import BeautifulSoup as bs
import pdb
import sys
import os
import cPickle

def crawl_site(poi, base_url, fout):
    poi_id = base_url.split('/')[-1].replace('html', '')
    ts = int(time.time() * 1000)
    comment_url_template = 'http://www.mafengwo.cn/gonglve/ajax.php?' \
                       'act=get_poi_comments&poi_id=%s' \
                       '&type=0&order=4&' \
                       'category=&page=%d&' \
                       'ts=%d'
    for page_id in xrange(1, 50):
        try:
            comment_url = comment_url_template % (poi_id, page_id, ts)
            print >> fout, '*' * 80

            req = urllib2.Request(url=comment_url)
            response = urllib2.urlopen(req)
            rp = response.read()
            rp = json.loads(rp)
            soup = bs(rp[u'html'][u'html'])
            for cmt in soup.find_all('p', {'class':'rev-txt'}):
                try:
                    print >> fout, cmt.string.encode('utf8')
                except:
                    continue
        except:
            pass
            break
    fout.close()

if __name__ == '__main__':
    furl = sys.argv[1]
    poi_id = {}
    with open(furl) as fin:
        line_id = 1
        for lineid, line in enumerate(fin):
            poi, url = line.strip().split('\t')
            poi_id[poi] = line_id
            with open(os.path.join('data',  str(line_id) + '.txt'), 'w') as fout:
                crawl_site(poi, url, fout)
            line_id += 1
    cPickle.dump(poi_id, open('poiid.pkl', 'w'))



