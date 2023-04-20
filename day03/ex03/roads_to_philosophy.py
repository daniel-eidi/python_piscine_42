#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup as bs
import sys

def validate():
    argc = len(sys.argv)
    if (argc != 2):
        print("Invalid entry")
        sys.exit(1)

def remove_between(text, start_delimiter, end_delimiter):
    while True:
        start = text.find(start_delimiter)
        end = text.find(end_delimiter, start)
        if start == -1 or end == -1:
            return text
        text = text[:start] + text[end + len(end_delimiter) :]

def find(search, counter):
    url = 'https://en.wikipedia.org'
    print(search.split('/')[2])
    req_query = requests.get(url + search)
    html = bs(req_query.text, 'html.parser')
    html = html.find(id = "mw-content-text")
    html = html.select('p > a')[0]['href']
    if (html == '/wiki/Philosophy'):
        print('Philosophy')
        print(str(counter) +  " roads from 42 (number) to philosophy !")
        return
    else:
        counter += 1
        find(html, counter)

def validate():
    argc = len(sys.argv)
    if (argc != 2):
        print("Invalid entry")
        sys.exit(1)

def main():
    validate()
    find('/wiki/'+ str(sys.argv[1].replace(' ','_')), 1)

if __name__ == "__main__":
    # validate()
    main()