import sys
import json
import math
from collections import Counter

file1 = open("RC_2015-01-01.txt",'r')

text_samples = open("text_samples.txt","w")

subreddits = ['obama','democrats','SocialDemocracy','Liberal','Republican']


for i, line in enumerate(file1):
	if i%2 == 0:
		j = i/2 + 1
		l = int(math.log(j)/math.log(2))
		if 2**l == j:
			print j
	#if i>100:
	#   	break
	try:
		#print line
		line_json = json.loads(line)
		author = line_json['author']
		if author == '[deleted]':
			continue
		subreddit = line_json['subreddit']
		#print subreddit
		if subreddit in subreddits:
			#print subreddit
			text_samples.write('-begin-'+'\t'+subreddit+'\t\n')
			text_samples.write(line_json['body']+'\n')

		#print line
	except:
		continue




