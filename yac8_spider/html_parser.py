#coding=utf-8

from bs4 import BeautifulSoup
import re
import urlparse
import logging
from yac8_spider import html_outputer
import urllib


class HtmlParser(object):
    
    def __init__(self):
        #设置logger
        logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)
#         logger = logging.getLogger('test')
#         fHandler = logging.FileHandler('test.log')
#         logger.addHandler(fHandler)
        self.outputer = html_outputer.HtmlOutputer()

    def _get_new_urls(self, page_url, soup):
        
        links = soup.find_all('a', href=re.compile(r"news/list_\d+\.html"))
        new_urls = set()
        
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url , new_url)
            new_urls.add(new_full_url)
            
        return new_urls
            
    
    
    def _get_new_data(self, page_url, soup):
#         parse data of html content
        # <ul class='subnav'><li><a href='news/list_97.html' target='_self' style=''>楷书字帖</a></li>
        url_nodes = soup.find_all('ul', class_='subnav')
        for url_node in url_nodes:
            res_data = {}
            nodes = url_node.find_all('a')
            for node in nodes:
                if node is None:
                    continue
                res_data['url'] = node['href']
                url_title = node.getText()
                if url_title is not None:
                    res_data['url_title'] = url_title
                else:
                    res_data['url_title'] = "NONE"
#                 print res_data['url']+','+res_data['url_title']
#             self.outputer.collect(res_data)
#             self.outputer.output_html()

        # <div class="a">   <h1>欧阳询75岁楷书《九成宫碑》玉山草堂本</h1>
#         image_title = soup.find('div', class_='a').find('h1')  #这里有问题
#         if image_title is not None:
#             res_data['image_title'] = image_title.getText()
#         else :
#             res_data['image_title'] = " NONE "
#         
        #<div id="newsContent"><div>
        #<img alt="欧阳询75岁楷书《九成宫碑》玉山草堂本" title="欧阳询75岁楷书《九成宫碑》玉山草堂本"   border="0" src="../upFiles/infoImg/201610/20161006065213246.jpg" />
        #<img alt="欧阳询75岁楷书《九成宫碑》玉山草堂本" title="欧阳询75岁楷书《九成宫碑》玉山草堂本"   border="0" src="../upFiles/infoImg/201610/20161006065212886.jpg" />
        #<img alt="欧阳询75岁楷书《九成宫碑》玉山草堂本" title="欧阳询75岁楷书《九成宫碑》玉山草堂本"   border="0" src="../upFiles/infoImg/201610/20161006065209493.jpg" /> 
#         image_urls = soup.find('div' , id="newsContent").findAll('img') 
#         for image_url in image_urls:
#             image_full_url = urlparse.urljoin(page_url, image_url)
# #            
#         res_data['image_local_url'] = image_full_url
        
        return None
    
    def _download_images(self,page_url, soup, index):
        imglist = soup.find_all('img')
        for imgurl in imglist:
            new_full_url = urlparse.urljoin(page_url , imgurl['src'])
            print new_full_url
            urllib.urlretrieve(new_full_url,'%s.jpg' %index )
            index += 1
    
    
    def parse_html(self, page_url, content, index):
        if page_url is None or content is None:
            return None
        
        soup = BeautifulSoup(content, 'html.parser')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        self._download_images(page_url, soup, index)
        return new_urls, new_data
    