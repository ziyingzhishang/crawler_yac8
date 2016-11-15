#coding=utf-8

class HtmlOutputer(object):
    
    
    def __init__(self):
        self.datas = []
    
    def collect(self,data):
        if data is None:
            return None
        self.datas.append(data)

    
    def output_html(self):
        fout = open('output.data', 'a')
        
        for data in self.datas:
#             fout.write(data['title'].encoding('utf-8'))
            fout.write(data['url'])
            fout.write(','+data['url_title'])
#             fout.write(','+data['image_title'])
            fout.write('\n')
            
        fout.close()
    
    
    
    



