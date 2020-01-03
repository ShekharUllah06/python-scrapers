'''
Created on Dec 30, 2019

@author: Abdullah
'''
from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

url='https://www.amazon.com/s?k=toys+for+2+year+old+girls&crid=J2SDSPVG6T5H&sprefix=%2Caps%2C451&ref=nb_sb_ss_i_1_0'
response = requests.get(url, headers=headers)
text=response.text.encode('utf-8')
soup = BeautifulSoup(text,"html.parser")
a=soup.findAll('a', attrs={'class':'a-link-normal a-text-normal'})

f= open("links.txt","w+")
k=0
for i in a:
    k=k+1
    try:
        print('https://www.amazon.com/'+i.get('href'))
        f.write('https://www.amazon.com/'+i.get('href')+'\n')
        print(k)
    except UnicodeEncodeError:
        continue

    
print(len(a))
