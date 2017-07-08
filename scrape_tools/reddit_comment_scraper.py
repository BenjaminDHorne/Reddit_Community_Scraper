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

import praw

reddit = praw.Reddit(user_agent='Comment Extraction (by /u/BDHResearch)',
                     client_id='4iq6UiKGMOE35w', client_secret="_YZhBJI7_2wjqTSHRZSBtOOY1QY",
                     username='BDHResearch', password='Bdbomb777')

def get_posts_with_id_collected():
    with open("post_links_done.txt") as done:
        links_collected = [link for link in done]
    return links_collected

def comment_scraper(sub, post_file):
    FORMAT = "%(asctime)s %(levelname)s %(module)s %(lineno)d %(funcName)s:: %(message)s"
    logging.basicConfig(filename=sub+'_comment.log', filemode='a', level=logging.DEBUG, format=FORMAT)
    warnings.filterwarnings("ignore")
    
    outfile = sub+'_postandcomment_data.json'

    logging.info("------> Starting comment Collection for "+post_file)
    links_collected = get_posts_with_id_collected()
    with open(outfile, "a") as out:
        with open(post_file) as postdata:
            for line in postdata:
                x=json.loads(line.strip())
                for child in x['data']['children']:
                    permalink = child['data']['permalink']
                    if permalink in links_collected:
                        continue
                    with open("post_links_done.txt", "a") as store:
                        store.write(str(permalink)+"\n")
                    page_link = "https://www.reddit.com"+permalink

                    submission = reddit.submission(url=page_link)
                    
                    #submission data extraction
                    data_dict = {}
                    sub_data = {"id": "t3_"+str(submission.id), "score": submission.score, "numcmts": submission.num_comments,"title":submission.title , "selftext":submission.selftext, "url":submission.url, "author":str(submission.author)} 
                    data_dict['submission'] = sub_data
                    
                    #comment data extraction
                    cmts_data = {}
                    submission.comments.replace_more(limit=0)
                    for comment in submission.comments.list():
                        cmt_data = {"body":comment.body,"score":comment.score,"depth":comment.depth, "author":str(comment.author), "parent":comment.parent_id}
                        cmts_data["t1_"+str(comment.id)] = cmt_data
                    data_dict["comments"] = cmts_data
                    out.write(json.dumps(data_dict)+"\n")
