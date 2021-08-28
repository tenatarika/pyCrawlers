# -*- coding: utf-8 -*-
"""
Created on Sun May  2 02:41:48 2021

@author: Furcas
"""

from DataSets import Content, Website
from bs4 import BeautifulSoup

import requests

class Crawler:
    def getPage(self, url: Website):
        try:
            req = requests.get(url)
        
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(req.text, 'lxml.parser')
    
    def safeGet(self, pageObj, selector):
        childObj = pageObj.select(selector)
        if childObj is not None and len(childObj) > 0:
            return childObj[0].get_text()
        return ''
    
    def search(self, topic, site: Website):
        """
        Поиск на заданном сайте  
        и сохранение всех найденных таблиц
        """
        bs = self.getPage(site.searchUrl + topic)
        searchResults = bs.select(site.resultListing)
        for result in searchResults:
            url = result.select(site.resultUrl)[0].attrs['href']
            if(site.absoluteUrl):
                bs = self.getPage(url)
            else:
                bs = self.getPage(site.url + url)
            if bs is None:
                print('Something was wrong with that page or URl. Skipping!!!')
                return 
            title = self.safeGet(bs, site.titleTag)
            body = self.safeGet(bs, site.bodyTag)
            if title != '' and body != '':
                content = Content(topic, title, body, url)
                content.print()
    
    
        
        
        
        
        
        
        
        
        
        
        
        