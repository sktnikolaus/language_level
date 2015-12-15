import pickle
import sys
import json
import math
import random
from collections import Counter

file2 = open("subreddit_to_author.p",'r')
object_file = pickle.load(file2)
print 'loaded1'

def count(writeflag):
	topic_counter = Counter()

	idx = 0
	for key,value in object_file.iteritems():
		topic_counter[key]=len(value)
		#print topic_counter
		#idx +=1
		#if idx>100000:
		#	break#sys.exit(-1)

	#mc = topic_counter.most_common(20000)
	mc = topic_counter
	
	if writeflag:
		output_file = open("counts_total.txt","w")
		output_file.write('counts\n')
		for topic,val in mc.iteritems():
			output_file.write(str(topic)+' '+str(val))
			output_file.write('\n')

		output_file.close()
	
	return mc

#mc = count(False)

print len(object_file.keys())

def determine_avg_no_users_per_topic(mc):
	output_file = open("avg_no_topics_per_avg_user_spec2.txt","w")
	output_file.write('avg_no_topics\n')

	#selections = mc[500:1500]#[1260:1310]#['TheHobbit','playstation','reptiles','Bonsai','Audi','gay','Boobies','medicine','Turkey','AppHookup']
	selections = random.sample(object_file.keys(),1000)
	#selections = ['democrats','Republican']

	file1 = open("author_to_subreddit.p",'r')
	object_file1 = pickle.load(file1)
	print len(object_file1.keys())
	for selection in selections:
		users = set(object_file[selection])
		avg_no_topics = 0
		for user in users:
			avg_no_topics += len(set(object_file1[user]))
		avg_no_topics = avg_no_topics/float(len(users))
		outputstring = selection+': '+str(avg_no_topics)
		output_file.write(outputstring)
		output_file.write('\n')

	output_file.close()

determine_avg_no_users_per_topic(None)

'''
for key,value in object_file.iteritems():
	print key,value
	sys.exit(-1)
'''