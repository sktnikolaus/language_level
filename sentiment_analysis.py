from textblob import TextBlob
import sys
import json
import math
from collections import Counter

file1 = open("text_samples.txt",'r')

sentiment_analysis = open("sentiment.txt","w")


for i, line in enumerate(file1):

	if line[0:7]=='-begin-':
		post = line.split('\t')
		topic = post[1]
	else:
		# split in sentences
		tb = TextBlob(line)
		#print tb.sentences
		for sentence in tb.sentences:
			senti = sentence.sentiment.polarity
			sub = sentence.sentiment.subjectivity
			sentiment_analysis.write(topic+'\t'+str(senti)+'\t'+str(sub)+'\n')
		#sys.exit(-1)
