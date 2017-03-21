import json
import sys
import unicodedata
import requests
import urllib3
from lxml import html
import time
import warnings
import logging


def get_reddit_data(sub, page_link):
    url_base = "https://www.reddit.com/r/"
    try:
        http = urllib3.PoolManager()
        r = http.request('GET', url_base+sub+"/.json"+page_link)
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
    num_posts_to_collect = 1000
    sub_to_collect = ""
    outfile = ""

    logging.info("------> Starting Collection for "+sub_to_collect)
    logging.info("------> Running Until End or "+str(num_posts_to_collect)+" Posts")
    logging.info("------> Writing Data out to "+outfile)
    with open(outfile, "a") as out:
        page_data = get_reddit_data(sub_to_collect, "")
        out.write(page_data+"\n")
        page = json.loads(page_data)
        after = page["data"]["after"]
        count = 25
        p_num = 1
        while after is not None and count <= num_posts_to_collect:
            logging.info("collecting page number "+str(p_num))
            logging.info("TOTAL POST COLLECTED = "+str(count))
            time.sleep(3)
            page_link = "?count="+str(count)+"&after="+after
            page_data = get_reddit_data(sub_to_collect, page_link)
            out.write(page_data+"\n")
            try:
                page = json.loads(page_data)
                after = page["data"]["after"]
            except:
                logging.warning("Error when loading json file")
            count+=25
            p_num+=1
