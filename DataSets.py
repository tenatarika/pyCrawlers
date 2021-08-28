# -*- coding: utf-8 -*-
"""
Created on Sat May  1 16:46:28 2021

@author: Furcas
"""

class Content:
    """
    Общий класс для страниц и статей 
    """
    def __init__(self, url, title, body, topic):
        self.url = url
        self.title = title
        self.body = body
        self.topic = topic
        
    def print(self):
        print('New article found for topic {self.topic}')
        print(f"URL-> {self.url}")
        print(f"TITLE-> {self.title}")
        print(f"BODY-> {self.body}")
        
        
class Website():
    """
    Структура сайта
    """
    def __init__(self, name, url, searchUrl, resultListing,
                 resultUrl, absoluteUrl, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.searchUrl = searchUrl
        self.resultListing = resultListing
        self.resultUrl = resultUrl
        self.absoluteUrl = absoluteUrl
        self.titleTag = titleTag
        self.bodyTag = bodyTag
        

        
        
        
        
    
    
    
    
    
    
    
    
    
    