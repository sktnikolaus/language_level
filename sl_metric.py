
from __future__ import division
import sys
import random
import numpy as np
from numpy import genfromtxt

class SentenceLengthMetric:
	def __init__(self):
		print 'Sentence length metric initialized'

	def get_metric(self,wordlist):
		sentencelist=wordlist.split('.')
		avg_sentence_length = np.mean([len(sentence.split(' ')) for sentence in sentencelist])
		return self.convert_length2score(avg_sentence_length)

	def convert_length2score(self,length):
		x = (length-2)*4/50
		result = np.tanh(x)
		return result*10.0
		
		
		

