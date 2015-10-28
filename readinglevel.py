
import sys
import random
import numpy as np
import itertools
from fb_metric import FrequencyBasedMetric
from sl_metric import SentenceLengthMetric

f = open('../data/cnn_na.txt','r')

applied_submetric_names = ['FrequencyBasedMetric','SentenceLengthMetric'] 

'''
# to be continued with more sophisticated methods:,
'GrammaticalMetric',..
'''

# Initialize all the metrics that should be used
metrics = []
for sub in applied_submetric_names:
	if sub == 'FrequencyBasedMetric':
		metric = FrequencyBasedMetric()
		metrics.append(metric)
	elif sub == 'SentenceLengthMetric':
		metric = SentenceLengthMetric()
		metrics.append(metric)
	else:
		pass

# Score each line of the test file with each single metric
total_score,labels = [],[]
for line in f:
	if line[:3]=='[N]':
		label='Normal'
	else:
		label='Abbreviated'
	
	sub_scores = []
	for metric in metrics:
		sub_scores.append(metric.get_metric(line[3:]))
	total_score.append(sub_scores)
	labels.append(label)

# Print the evaluation results
for score,label in itertools.izip(total_score,labels):
	print 'Eval:',score,label
