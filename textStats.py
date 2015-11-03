
from __future__ import division
import string
import re
from tabulate import tabulate
from os import listdir

def count_char(text, ignore_spaces = True):
	if not ignore_spaces:
		return len(text.replace(' ', ''))
	return len(text)

def count_lexicon(text, remove_ponctuation = True):
 	exclude = list(set(string.punctuation))
 	if remove_ponctuation:
 		text = ''.join(ch for ch in text if ch not in exclude)
 		return len(text.split())
 	return len(text.split())

def count_syllable(text):
	count = 0
	vowels = 'aeiouy'
	text = text.lower().strip(".:;?!)(")
	if text[0] in vowels:
	    count += 1
	for index in range(1, len(text)):
	    if text[index] in vowels and text[index-1] not in vowels:
	        count += 1
	if text.endswith('e'):
	    count -= 1
	if text.endswith('le'):
	    count += 1
	if count == 0:
	    count += 1
	count = count - (0.1*count)
	return (round(count))

def count_sentence(text):
	count = len([w for w in re.split('[;.!?]', text) if w!=''])
	if text[len(text)-1] in [';', '.', '!', '?']:
		count -= 1
	return count

def get_statistics(filename, number_of_line = float('Inf'), verbose = True, directory = ''):
	'''
	Input :
	- filename (string) : name of the txt file that we want to analyze
	- number_of_line (int) : number of line that we want to look at, by default we look at the whole file

	Output :
	- number of characters
	- number of words
	- number of sentences
	'''
	file = open(directory+filename, 'r')
	
	numChar = 0
	numLexicon = 0
	numSentence = 0
	numSyllable = 0

	for line in file:
		numChar += count_char(line)
		numLexicon += count_lexicon(line)
		numSentence += count_sentence(line)
		numSyllable += count_syllable(line)
	#print filename
	# if verbose:
	# 	l = 30
	# 	print '{:<l} = {:>8}'.format('# characters', numChar)
	# 	print '{:<l} = {:>8}'.format('# words', numLexicon)
	# 	print '{:<l} = {:>8}'.format('# sentences', numSentence)
	# 	print '{:<l} = {:>8}'.format('# syllable', numSyllable)
	# 	print '{:<l} = {:>8}'.format('avg size of sentences', numLexicon/numSentence)
	# 	print '{:<l} = {:>8}'.format('avg size of words (char)', numChar/numLexicon)
	# 	print '{:<l} = {:>8}'.format('avg size of words (syllable)', numSyllable/numLexicon)
	fleschIndex = 206.835 - 1.015*(numLexicon/numSentence) - 84.6*(numSyllable/numLexicon)
	return [filename[:-4], 
	numChar, numLexicon, numSentence, numSyllable, 
	numLexicon/numSentence, numChar/numLexicon, numSyllable/numLexicon,
	fleschIndex]


def analyze_corpus(directory):
	filelist = listdir(directory)
	txtfilelist = [filename for filename in filelist if filename[len(filename)-4:] == '.txt']
	statistics = []
	
	header = ['Name', 
	'# characters', 
	'# words', 
	'# sentences', 
	'# syllables',
	'avg size of sentences', 
	'avg size of words (char)', 
	'avg size of words (syllable)',
	'flesh index']

	for filename in txtfilelist:
		statistics.append(get_statistics(filename, verbose = False, directory = directory))
	return tabulate(statistics, headers = header)


directory = '../corpus/'
print analyze_corpus(directory)






