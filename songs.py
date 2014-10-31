import praw
import re

user_agent = "Song finder bot (read only) by /u/XiiencE"
api = praw.Reddit(user_agent=user_agent)

threads = api.search("songs that", subreddit="askreddit", limit=10)
# http://blog.lucascaton.com.br/index.php/2012/04/10/regex-to-match-youtube-urls-using-ruby/
regex = re.compile("(?:https?:\/\/)?(?:www\.)?youtu(?:\.be|be\.com)\/(?:watch\?v=)?([\w-]{10,})")

for thread in threads:
    print thread.title
    for comment in thread.comments:
        # http://stackoverflow.com/questions/17430409/in-praw-im-trying-to-print-the-comment-body-but-what-if-i-encounter-an-empty
        if not hasattr(comment, 'body'):
            continue
        match = regex.search(comment.body)
        if match:
            print match.group()
