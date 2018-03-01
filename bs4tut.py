from bs4 import BeautifulSoup as bs
import requests

soup = ''
count = 0

def download(my_url):
    html = requests.get(my_url).text
    soup = bs(html,'html.parser')
    return soup

def printAll(tag):
    containers = soup.findAll(tag)
    print('*'*10+'YOUR DATA'+'*'*10)
    for container in containers:
        print(container.text)
    print('*'*29)

while True:
    if count>0:
        print('\n')
    print('Options - enter to exit\n\t1. download(url) - returns the soup.\n'
            +'\t2. printAll(soup.find_all(tag) - list all of text found in these tags.\n'
            +'3. I will make more functions')
    i = input('Enter a number representing a function: ')
    if i==str(1):
        p = input('Enter a url: ')
        soup = download(p)
    if i==str(2):
        p = input('Enter a tag: ')
        printAll(p)
    count+=1
    if not i:
        break
