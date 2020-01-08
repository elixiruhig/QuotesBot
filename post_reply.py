import praw
import pdb
import re
import os
import pandas as pd
import random

reddit = praw.Reddit('bot1')
data = pd.read_csv('QUOTE.csv')
quotes = []
for i in range(len(data)):
	quotes.append(data.iloc[i].quote)

if not os.path.isfile('submission_check.txt'):
	posts_replied_to = []
else:
	with open('submission_check.txt','r') as f:
		posts_replied_to = f.read()
		posts_replied_to = posts_replied_to.split('\n')
		posts_replied_to = list(filter(None, posts_replied_to))
subreddit = reddit.subreddit('pythonforengineers')
for submission in subreddit.hot(limit=10):
	if submission.id not in posts_replied_to:
		if re.search('I love Python',submission.title, re.IGNORECASE):
			submission.reply(quotes[random.randrange(0,36165,1)])
			posts_replied_to.append(submission.id)

with open('submission_check.txt','w') as f:
	for post_id in posts_replied_to:
		f.write(post_id + "\n")
