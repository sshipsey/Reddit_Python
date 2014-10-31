import praw
import pprint
from parse import *
from parse import compile
user_agent = ("Song finder bot (read only) by /u/XiiencE")
r = praw.Reddit(user_agent=user_agent)

subreddit = r.get_subreddit('askreddit')
threads = r.search("songs that",subreddit="askreddit",limit=10)
text = "(http://{})"
for thread in threads:
	pprint.pprint(thread.title)
	comments = thread.comments
	for comment in comments:

		if search(text,comment.body) != None:
			pprint.pprint(search(text,comment.body)[0])

			
	#look for youtube links
