#!/usr/bin/env python

import sys

import scrape_tools.reddit_post_scraper as post_scraper
import scrape_tools.reddit_comment_scraper as comment_scraper

number_posts_to_collect = 300000
with open("subs_to_collect.txt") as subs:
    subs_to_collect = [l.strip() for l in subs]

for sub_to_collect in subs_to_collect:
    post_scraper(number_posts_to_collect, sub_to_collect)
    post_file = sub_to_collect+"_reddit_posts.json"
    comment_scraper(sub_to_collect, post_file)
