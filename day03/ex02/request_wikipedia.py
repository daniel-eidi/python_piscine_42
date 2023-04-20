#!/usr/bin/python3

import requests
import json
import dewiki
import sys

def validate():
    argc = len(sys.argv)
    if (argc != 2):
        print("Invalid entry")
        sys.exit(1)

search = sys.argv[1].replace(' ','_')
print(search)

def remove_between(text, start_delimiter, end_delimiter):
    while True:
        start = text.find(start_delimiter)
        end = text.find(end_delimiter, start)
        if start == -1 or end == -1:
            return text
        text = text[:start] + text[end + len(end_delimiter) :]

def main():
    params_query = {
        'action' : 'query',
        'prop' : 'extracts',
        'redirects' : True,
        'titles' : search,
        'format' : 'json',
    }
    req_query = requests.get('http://en.wikipedia.org/w/api.php', params=params_query)
    page_id = list(req_query.json()['query']['pages'].keys())[0]
    if (page_id == '-1'):
        print("Information not found, server problem or any other problem.")
        return
    else:
        req_parse(page_id)
    
def req_parse(page_id):
    params_parse = {
        'action' : 'parse',
        'prop' : 'wikitext',
        'pageid' : page_id,
        'format' : 'json'
    }
    req_parse = requests.get('http://en.wikipedia.org/w/api.php', params=params_parse)
    txt = dewiki.from_string((req_parse.json())['parse']['wikitext']['*']).strip()
    txt = remove_between(str(txt), '{{', '}}')
    with open(sys.argv[1] + '.wiki', 'w') as file:
        file.write(str(txt))

    print(txt)

if __name__ == "__main__":
    # validate()
    main()