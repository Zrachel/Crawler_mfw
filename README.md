# Crawler_mfw
a selenium and bs4 based python crawler

---------------------------------------------
������selenium����

1. ���ߣ����Թ���seleniumģ����ҳʵ�ʵ������ (+BeautifulSoup������ҳ����) 
2. ������centos

�������������⣺
1. selenium.common.exceptions.WebDriverException: Message: connection refused
-------
ȥ��geckodriver.log 


2. selenium.common.exceptions.WebDriverException: Message: Failed to start browser: entity not found
-------
��binary = FirefoxBinary(���·��)�ĳ�binary = FirefoxBinary(����·��)����֤·����ȷ


3. Python Selenium Webdriver Failed to star browser: Permission denied
����
selenium.common.exceptions.WebDriverException: Message: Failed to start browser: entity not found
-------
ָ��firefoxĿ¼��������ʾ��

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


binary = FirefoxBinary('firefox�����ƿ�ִ���ļ��ľ���·��')
driver = webdriver.Firefox(firefox_binary=binary)

driver.get('��Ҫ����url')
html = driver.page_source       

from bs4 import BeautifulSoup
soup = BeautifulSoup(html)
soup.find('p', attrs={'class':'classname'})

elems = driver.find_elements_by_class_name("multiclass1.multiclass2")
for elem in elems:
		print elem.get_attribute('��Ҫ��attribute')



4. Error: no display specified
-------
export DISPLAY=:0


5. Error: cannot open display: :0
-------
���������һ��û��GUI�Ļ����²�������ô����Ҫһ��headless����������xvfb�������Ҹ���gui�ķ�����Ȼ����ssh + Xming���ʡ���
xvfb���ԣ�http://www.alittlemadness.com/2008/03/05/running-selenium-headless/
��gui�Ļ������ԣ�http://blog.sina.com.cn/s/blog_60230cd90100j98e.html





Docs:
1. selenium�ٷ��ĵ���http://selenium-python.readthedocs.io/installation.html ��˵ʵ������ȫ������java�Ľӿ�ȫһЩ���õ���Ҳ��
2. selenium��run javascript��http://stackoverflow.com/questions/5585343/getting-the-return-value-of-javascript-code-in-selenium/5585345#5585345



