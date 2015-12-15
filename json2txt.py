import sys
import json

#text_samples = open("democrats.json","r")
text_samples = open("republican.json","r")
#text_samples = open("obama.json","r")
#text_samples = open("politics.json","r")



#out = open('topic_sql_democrats.txt','w')
out = open('topic_sql_republican.txt','w')
#out = open('topic_sql_obama.txt','w')
#out = open('topic_sql_politics.txt','w')


#subreddits = ['Republican']#,'SocialDemocracy','Liberal','Republican']

for line in text_samples:
	try:
		line_json = json.loads(line)
		out.write(line_json['body'])
	except:
		continue
		#print line
		#sys.exit(-1)
out.close()


#inp = open('topic_sql_democrats.txt','r')
#out = open('topic_sql_democrats_clean.txt','w')
#'''

inp = open('topic_sql_republican.txt','r')
out = open('topic_sql_republican_clean.txt','w')
'''
inp = open('topic_sql_obama.txt','r')
out = open('topic_sql_obama_clean.txt','w')

#inp = open('topic_sql_politics.txt','r')
#out = open('topic_sql_politics_clean.txt','w')
'''

for line in inp:
	if line[0:3]=='[**':
		continue
	else:
		out.write(line)



