import praw
import pandas as pd

reddit = praw.Reddit(client_id='emUff7fdtvmK6w',
                     client_secret='npXpD8mpU-FdMED9v22cxSJFsrw',
                     user_agent='PrawTut')

# ? from 21.12.2018 to 31.12.2018 
idList = ['ab4spi', 'aatrgw', 'aaj21h', 'aa803q', 'a9wxyx', 'a9mgdl',
          'a9cwfm', 'a92rwb', 'a8sqj9', 'a8iryx', 'a87fn8']

commentList = []

for item in idList:
    submission = reddit.submission(id=item)
    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
        commentList.append(comment.body)

commentList = list(map(lambda x:x.strip(), commentList))

df = pd.DataFrame({'document':commentList})
df['type'] = 1

file_name = 'bitcoin_comments.csv'
df.to_csv(file_name, sep='\t')