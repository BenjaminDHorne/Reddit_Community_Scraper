import json
import sys
import unicodedata
import requests
import urllib3
from lxml import html
import time
import warnings
import logging
import json


def get_reddit_data(page_link):
    url_base = "https://www.reddit.com"
    try:
        http = urllib3.PoolManager()
        r = http.request('GET', url_base+page_link)
        if len(r.data) == 0:
            logging.warning("Data came back with 0 length")
            return None
        return r.data.decode('utf-8').strip()
    except:
        logging.warning("Something General went wrong with scrape, Maybe check your internet connection")



if __name__ == '__main__':
    FORMAT = "%(asctime)s %(levelname)s %(module)s %(lineno)d %(funcName)s:: %(message)s"
    logging.basicConfig(filename='common.log', filemode='a', level=logging.DEBUG, format=FORMAT)
    
    warnings.filterwarnings("ignore")
    post_file = '_reddit_data.json'
    outfile = '_reddit_comments.json'
    
    #go through line by line, load json

    logging.info("------> Starting comment Collection for "+post_file)
    with open(outfile, "a") as out:
        with open(post_file) as postdata:
            for line in postdata:
                x=json.loads(line.strip())
                for child in x['data']['children']:
                    permalink = child['data']['permalink']
                    page_link = permalink[:-1]+".json"
                    page_data = get_reddit_data(page_link)
                    out.write(page_data+"\n")
        
