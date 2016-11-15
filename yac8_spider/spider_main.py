#encoding=utf-8

from yac8_spider import html_downloader, html_parser, url_manager, html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
        self.index = 0
    
    def crow(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
#                 print 'number %d : %s' %(count, new_url)
                html_content = self.downloader.download(new_url)
                new_urls , new_data = self.parser.parse_html(new_url, html_content, self.index)
                self.urls.add_new_urls(new_urls)
#                 self.outputer.collect(new_data)
                
                count = count + 1
                
            except:
                print 'craw failed %s ' %(new_url)
         
#         self.outputer.output_html()
    
if __name__ == "__main__":
    root_url = "http://www.yac8.com/"
    obj_spider = SpiderMain()
    obj_spider.crow(root_url)
    