
from __future__ import division
import sys
import random
import numpy as np
from numpy import genfromtxt

class FrequencyBasedMetric:
	def __init__(self):
		f = open('../data/4000words.csv','r')
		self.common_words = [x.strip('\n').rstrip() for x in f.readlines()]
		print 'frequency based Metric initialized'

	def get_metric(self,wordlist):
		wordlist = wordlist.split(' ')
		no_words = len(wordlist)
		commonwords = sum([1 for word in wordlist if word in self.common_words])
		ratio = commonwords/no_words
		score = self.convert_ratio2score(ratio)
		return score

	def convert_ratio2score(self,ratio):
		# 100% corresponds to 0
		# 0 % corresponds to 10 (needs to be adjusted and calibrated)
		return (1-ratio)*10
		
		

