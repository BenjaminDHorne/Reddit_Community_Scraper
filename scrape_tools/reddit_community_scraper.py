import json
import sys
import unicodedata
import requests
import urllib3
import urllib2
from lxml import html
import time
import warnings
import logging
import json

import praw

reddit = praw.Reddit(user_agent='Post and Comment Extraction (by /u/BDHResearch)',
                     client_id='4iq6UiKGMOE35w', client_secret="_YZhBJI7_2wjqTSHRZSBtOOY1QY",
                     username='BDHResearch', password='Bdbomb777')

def fix(text):
    text = text.decode("ascii", "ignore")
    return text

def internet_on():
    try:
        urllib2.urlopen('http://www.google.com', timeout=20)
        return True
    except urllib2.URLError as err: 
        return False

def get_posts_with_id_collected():
    with open("post_links_done.txt") as done:
        links_collected = [link for link in done]
    return links_collected

def scraper(sub, date_range, outfile, collect_posts=True, collect_cmts=True):
    FORMAT = "%(asctime)s %(levelname)s %(module)s %(lineno)d %(funcName)s:: %(message)s"
    logging.basicConfig(filename=sub+'.log', filemode='a', level=logging.DEBUG, format=FORMAT)
    warnings.filterwarnings("ignore")

    #check internet connection before start
    while internet_on() == False:
        print "Internet connection issue, sleeping for 60 seconds..."
        logging.warning("Internet connection issue, sleeping for 60 seconds...")
        time.sleep(60)
        print "Waking up and Trying again..."
        
    #scraper    
    with open(outfile, "a") as out:
        for submission in reddit.subreddit(sub).submissions(date_range[0], date_range[1]):
            tryagain = True
            while tryagain:
                try:
                    if collect_posts:
                        #submission data extraction
                        data_dict = {}
                        sub_data = {"id": "t3_"+str(submission.id), "score": submission.score, "numcmts": submission.num_comments,"title":submission.title , "selftext":submission.selftext, "url":submission.url, "author":str(submission.author), "is_self":submission.is_self} 
                        data_dict['submission'] = sub_data

                    if collect_cmts:
                        #comment data extraction
                        cmts_data = {}
                        submission.comments.replace_more(limit=0)
                        for comment in submission.comments.list():
                            cmt_data = {"body":comment.body,"score":comment.score,"depth":comment.depth, "author":str(comment.author), "parent":comment.parent_id}
                            cmts_data["t1_"+str(comment.id)] = cmt_data
                        data_dict["comments"] = cmts_data

                    #output to file
                    out.write(json.dumps(data_dict)+"\n") #every line is a submission dictionary

                    #set tryagain flag
                    tryagain = False
                except KeyboardInterrupt:
                    logging.info('Termination received. Goodbye!')
                    tryagain = False
                except:
                    logging.exception('ran into an error, trying again')
                    time.sleep(10)
                    tryagain = True
                                
