# Reddit_Community_Scraper
General Subreddit Scraper that first scrapes posts, then scrapes comments under those posts. 

To use the scraper:

1. Create list of subreddits in file subs_to_collect.txt, where each is on a newline
2. Provide UTC timestape for start date and end date variables in scraper_run.py
3. To collect both posts and comments, use 'scraper.scraper(sub, (start_date, end_date), outfile, True, True)' in scraper_run.py. To collect only posts use 'scraper.scraper(sub, (start_date, end_date), outfile, True, False)'.
4. In scrape_tools/reddit_community_scraper.py provide API client information. This can be done from any reddit account. 


