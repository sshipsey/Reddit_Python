import praw
import re

user_agent = "Song finder bot (read only) by /u/XiiencE"
api = praw.Reddit(user_agent=user_agent)

threads = api.search("songs that", subreddit="askreddit", limit=10)

linkregex = re.compile("(?:https?:\/\/)?(?:www\.)?youtu(?:\.be|be\.com)\/(?:watch\?v=)?([\w-]{10,})")

textregex = re.compile("(?<=\[)[^\]]*(?=\])")

f = open('Playlist.html', 'w')

f.write('<div><ul>')

i = 0
j = 0

for thread in threads:
    f.write('<li>' + thread.title + '</li>')
    j = 0
    for comment in thread.comments:
        if not hasattr(comment, 'body'):
            continue
        match = linkregex.search(comment.body)
        text = textregex.search(comment.body)
        if match and text:
            #print match
            #print text
            string = '<li><a href=' + match.group() + '>' + text.group() + '</a></li>'
            string = string.encode('ascii','ignore')
            f.write(string)
        j += 1
        if j >= 20:
        	break
    i += 1
    if i >= 10:
    	break
f.write('</ul></div>')
f.close()