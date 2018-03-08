# Reddit_Community_Scraper
General Subreddit Scraper that first scrapes posts, then scrapes comments under those posts. 

To use the scraper:

1. create list of subreddits in file subs_to_collect.txt, where each is on a newline
2. provide UTC timestape for start date and end date variables in scraper_run.py
3. To collect both posts and comments, use 'scraper.scraper(sub, (start_date, end_date), outfile, True, True)' in scraper_run.py. To collect only posts use 'scraper.scraper(sub, (start_date, end_date), outfile, True, False)'.

If used, please cite "Horne, Benjamin D., Sibel Adali, and Sujoy Sikdar. "Identifying the social signals that drive online discussions: A case study of Reddit communities." arXiv preprint arXiv:1705.02673 (2017)."
