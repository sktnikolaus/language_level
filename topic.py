import sys
import json
import math

#file1 = open("text_samples.txt",'r')

text_samples = open("text_samples.txt","r")

out = open('topic_replublicans.txt','w')

subreddits = ['Republican']#,'SocialDemocracy','Liberal','Republican']

for line in text_samples:
	if line[0:7]=='-begin-':
		post = line.split('\t')
		topic = post[1]
	else:
		if topic==subreddits[0]:
			out.write(line)





