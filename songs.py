import praw
import re

user_agent = "Song finder bot (read only) by /u/XiiencE"
api = praw.Reddit(user_agent=user_agent)

threads = api.search("songs that", subreddit="askreddit", limit=10)

linkregex = re.compile("(?:https?:\/\/)?(?:www\.)?youtu(?:\.be|be\.com)\/(?:watch\?v=)?([\w-]{10,})")

textregex = re.compile("(?<=\[)[^\]]*(?=\])")

f = open('Playlist.html', 'w')

f.write('<body style="background-color: #b0c4de"><h1>Reddit\'s Playlist:</h1><div>')

i = 0
j = 0

for thread in threads:
    j = 0
    itemstring = ''
    for comment in thread.comments:
        if not hasattr(comment, 'body'):
            continue
        match = linkregex.search(comment.body)
        text = textregex.search(comment.body)
        titlestring = '<div style="font-size:110%"><b>' + thread.title + '</b></div><ul>'
        if match and text:
            itemstring += '<li><a href=' + match.group() + '>' + text.group() + '</a></li>'
        j += 1
        if j >= 20:
        	break
    if itemstring:
    	f.write(titlestring)
    	itemstring = itemstring.encode('ascii','ignore')
    	f.write(itemstring)
    i += 1
    f.write('</ul>')
    if i >= 10:
    	break
f.write('</ul></div></body>')
f.close()