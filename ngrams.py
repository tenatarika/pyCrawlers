# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 03:20:33 2021

@author: Furcas
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re 

def get_Ngrams(content, n):
    content = re.sub('\n|[[\d+\]]', ' ', content)
    content = bytes(content, 'UTF-8')
    content = content.decode('ascii', 'ignore')
    content = content.split(" ")
    content = [word for word in content if word != '']
    output = []
    
    for i in range(len(content)-n+1):
        output.append(content[i:i+n])
    return output

html = urlopen('https://ru.wikipedia.org/wiki/%D0%9C%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0')
bs = BeautifulSoup(html, 'lxml')

content = bs.find('div', {'id': 'mw-content-text'}).get_text()
ngrams = get_Ngrams(content, 2)

print(ngrams)

print(f'2-grams count is {len(ngrams)}')

