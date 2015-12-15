'''
intro_data = [
  {
    "from": "cfdb28d752d5e05bea53de45",
    "n": 1,
    "to": "40b4a95eb677c2a24eb093115d5877b75783c7b6",
    "data": [
      {
        "tag": "Materials",
        "frequency": 1
      }
    ]
  }
'''

import pickle
import sys
import json
import math
from collections import Counter

print 'loading...'

reddit_author_file = open("subreddit_to_author.p",'r')
reddit_author = pickle.load(reddit_author_file)

print 'loaded1'

author_reddit_file = open("author_to_subreddit.p",'r')
author_reddit = pickle.load(author_reddit_file)

subreddits = ['democrats','Republican']

print 'loaded2'

''''
authors_demo = reddit_author['democrats']
authors_repu = reddit_author['Republican']

set_demo = set(authors_demo)
set_repu = set(authors_repu)

len_demo = len(set_demo)
len_repu = len(set_repu)
len_inter = len(set_demo.intersection(set_repu))

print len_demo, len_repu, len_inter
'''



result_list=[]
for subreddit in subreddits:
  authors = reddit_author[subreddit]

  for author in authors:
    #print author
    subs = author_reddit[author]
    for sub in subs:
      topic = 't_'+sub
      sub_dict={'from':author,'to':topic,'n': 1,'data':[{"tag": "Materials","frequency": 1}]}
      result_list.append(sub_dict)
      #print sub_dict
      #sys.exit(-1)

output_file = open('result2.txt','w')
#output_file.write(result_list)
#output_file.close()

#pickle.dump(result_list, open( 'result.txt', "wb" ) )


#parsed = json.loads(result_list)
output_file.write(json.dumps(result_list, indent=2, sort_keys=True))
