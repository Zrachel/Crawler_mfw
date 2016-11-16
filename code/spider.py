from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from bs4 import BeautifulSoup
import sys
import re
import os
import pdb

##binary = FirefoxBinary('/home/core/zhangruiqing/project/travel/code/getdata/tools/firefox/firefox')
#binary = FirefoxBinary('//root/zhangruiqing01/project/travel/code/getdata/tools/firefox/firefox')
#driver = webdriver.Firefox(firefox_binary=binary)
#
#driver.get('http://www.mafengwo.cn/poi/10123-2-69.html')
#html = driver.page_source       
#
#soup = BeautifulSoup(html)
#soup.find('p', attrs={'class':'rev-txt'})
#
#elems = driver.find_elements_by_class_name("pi._j_pageitem")
#for elem in elems:
#    if elem.get_attribute('data-page') == str(pageid):
#        elem.click()

class Crawler:
    def __init__(self):
        binary = FirefoxBinary('/root/zhangruiqing01/project/travel/code/getdata/tools/firefox/firefox')
        self.driver = webdriver.Firefox(firefox_binary=binary)

    def getcontent(self, html):
        cont = []
        soup = BeautifulSoup(html)
        comments = soup.find_all('p', attrs={'class':'rev-txt'})
        poi = soup.find('div', {'class':'s-title'}).findChild('h1').contents[0].encode('utf8')
        for comment in comments:
            content = comment.get_text().encode('utf8')
            cont.append(content)
        return poi, cont

    def writef(self, poi, conts):
        for cont in conts:
            cont = re.sub(r'\n','',cont)
            print >> self.fout, '\t'.join([poi, cont])

    def load_page_and_getcontent(self):
        html = self.driver.page_source
        poi, conts = self.getcontent(html)
        self.writef(poi, conts)
        elems = self.driver.find_elements_by_class_name("pi._j_pageitem")
        print >> sys.stderr, 'page', str(self.pageid), '...'
        self.driver.implicitly_wait(4)
        return elems

    def websiteInit(self, url):
        def checkfname(pageurl):
            fname = os.path.join('data', pageurl + '.txt')
            coid = 1
            while os.path.exists(fname):
                fname = os.path.join('data', pageurl + '_' + str(coid) + '.txt')
                coid += 1
            return fname

        self.pageid = 1
        self.pageurl_id = url.split('/')[-1][0:-5]
        self.fname = checkfname(self.pageurl_id)
        try:
            self.fout = open(self.fname, 'w')
        except:
            self.pageurl_id = str(random.randint(100000,1000000))
            self.fname = checkfname(self.pageurl_id)
            self.fout = open(self.fname, 'w')


    def crawl(self, source_url):
        source_url = source_url.strip()
        print >> sys.stderr, "loading from page", source_url
        self.driver.get(source_url)
        currenturl = self.driver.current_url
        if currenturl != source_url:
            print >> sys.stderr, source_url + 'not exists.\n'
            return
        print >> sys.stderr, "begin crawling"
        try:
            self.websiteInit(source_url)
            elems = self.load_page_and_getcontent()
            print >> sys.stderr, "getting", source_url, "from page 1"
            while True:
                flag = False
                self.pageid += 1
                for elem in elems:
                    if elem.get_attribute('data-page') == str(self.pageid):
                        elem.click()
                        flag = True
                        break
                if not flag:
                    break
                else:
                    elems = self.load_page_and_getcontent()
            self.fout.close()
        except:
            self.fout.close()
            os.popen('rm ' + self.fname)
            pass

def load_urlist(fin):
    urlist = fin.readlines()
    print >> sys.stderr, "totally", len(urlist), "urls"
    return urlist

if __name__ == '__main__':
    crawler = Crawler()
    with open(sys.argv[1]) as fin:
        urlist = load_urlist(fin)
    for url in urlist:
        crawler.crawl(url)
    #crawler.crawl('http://www.mafengwo.cn/poi/9349673.html') # napahai1
    #crawler.crawl('http://www.mafengwo.cn/poi/17848.html') # napahai2
    #crawler.crawl('http://www.mafengwo.cn/poi/10001-1-1.html') # napahai2
    #crawler.crawl('http://www.mafengwo.cn/jd/10442/tc?pn=11&m=0&src=www.mafengwo.cn/poi/5806.html') # napahai2



