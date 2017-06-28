'''
Created on 2017年6月28日

@author: wyq
'''
import urllib.request, string

class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None
        url = urllib.parse.quote(url, safe = string.printable) # 中文url转码
        response = urllib.request.urlopen(url)
        
        if response.getcode() != 200:
            return None
        return response.read()

