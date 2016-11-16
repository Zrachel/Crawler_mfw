# Crawler_mfw                                    
a selenium and bs4 based python crawler

---------------------------------------------


## 服务器selenium爬虫

1. 工具：测试工具selenium模拟网页实际点击操作 (+BeautifulSoup用于网页解析) 

2. 环境：centos

## Docs:
1. selenium官方文档：http://selenium-python.readthedocs.io/installation.html 但说实话并不全，还是java的接口全一些，用的人也多

2. selenium中run javascript：http://stackoverflow.com/questions/5585343/getting-the-return-value-of-javascript-code-in-selenium/5585345#5585345
-------

## 可能遇到的问题：

1. selenium.common.exceptions.WebDriverException: Message: connection refused
-------
去看geckodriver.log 


2. selenium.common.exceptions.WebDriverException: Message: Failed to start browser: entity not found
-------
把binary = FirefoxBinary(相对路径)改成binary = FirefoxBinary(绝对路径)并保证路径正确


3. Python Selenium Webdriver Failed to star browser: Permission denied 或者 selenium.common.exceptions.WebDriverException: Message: Failed to start browser: entity not found
-------
指定firefox目录，如下所示：

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


binary = FirefoxBinary('firefox二进制可执行文件的绝对路径')
driver = webdriver.Firefox(firefox_binary=binary)

driver.get('你要爬的url')
html = driver.page_source       

from bs4 import BeautifulSoup
soup = BeautifulSoup(html)
soup.find('p', attrs={'class':'classname'})

elems = driver.find_elements_by_class_name("multiclass1.multiclass2")
for elem in elems:
	print elem.get_attribute('你要的attribute')



4. Error: no display specified
-------
export DISPLAY=:0


5. Error: cannot open display: :0
-------
如果你是在一个没有GUI的环境下操作，那么你需要一个headless环境，比如xvfb；或者找个有gui的服务器然后用ssh + Xming访问。。
xvfb攻略：http://www.alittlemadness.com/2008/03/05/running-selenium-headless/
有gui的环境攻略：http://blog.sina.com.cn/s/blog_60230cd90100j98e.html


