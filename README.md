# Reddit_Community_Scraper
General Subreddit Scraper that first scrapes posts, then scrapes comments under those posts. 

To use the scraper:

1. Create list of subreddits in file subs_to_collect.txt, where each is on a newline
2. Provide UTC timestape for start date and end date variables in scraper_run.py
3. To collect both posts and comments, use 'scraper.scraper(sub, (start_date, end_date), outfile, True, True)' in scraper_run.py. To collect only posts use 'scraper.scraper(sub, (start_date, end_date), outfile, True, False)'.
4. In scrape_tools/reddit_community_scraper.py provide API client information. This can be done from any reddit account. 

----------------------------------------------------------------------------------------------------------------------------------------

Copyright (c) 2017, Benjamin D. Horne

All rights reserved.

Redistribution and use in any form, with or without modification, are permitted provided that the above copyright notice, this list of conditions and the following disclaimer are retained.

THIS CODE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
