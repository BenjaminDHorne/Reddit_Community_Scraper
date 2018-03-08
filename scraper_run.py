#!/usr/bin/env python

import sys
import os

import scrape_tools.reddit_community_scraper as scraper

start_date = "1492236000" #April 15th
end_date = "1500098400" #July 15th
with open("subs_to_collect.txt") as subs:
    subs_to_collect = [l.strip() for l in subs]

for sub in subs_to_collect:
    outfile = sub+"_postdata_"+start_date+"-"+end_date+".json"
    scraper.scraper(sub, (start_date, end_date), outfile, True, False) # First boolean param is for collecting posts, second boolean param is for collecting comments
