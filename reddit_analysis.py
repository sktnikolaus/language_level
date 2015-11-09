import sys
import random
import numpy as np
import itertools
import json

f = open('RC_2015-01-01.txt','r')


# Initialize all the metrics that should be used

# Score each line of the test file with each single metric

vertices_users = {}
vertices_topics = []

# otherwise it takes forever
ml=100000

for idx,line in enumerate(f):
	#line=line.split('\t')[2]
	try:
		#print idx
		json_line = json.loads(line)
		#print json_line

		author=json_line['author']
		subreddit=json_line['subreddit']

		if author in vertices_users.keys():
			vertices_users[author].append(subreddit)
		else:
			vertices_users[author]=[subreddit]

		vertices_topics.append(subreddit)

		if idx>ml:
			break#sys.exit(-1)
	except:
		if idx>ml:
			break#sys.exit(-1)

# analyze
print 'topic length',len(vertices_topics)
max_len, min_len,avg_len=0,0,0
no_topics_per_user=[len(topics) for topics in vertices_users.itervalues()]

np_topics_per_user=np.array(no_topics_per_user)
sorted_np = sorted(np_topics_per_user)[::-1]#.argsort()[-3:]#[::-1]
print sorted_np[:10]

max_len=max(no_topics_per_user)
avg_len=np.mean(no_topics_per_user)

print max_len,avg_len

