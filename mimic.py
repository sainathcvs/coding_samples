'''
Google PyQuick class exercise

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates.
'''

import sys
import random
def get_word_count(lines_arr):
	word_count={}
	for word in lines_arr:
		if word not in word_count.keys():
			word_count[word] = 1
		else:
			word_count[word]=word_count[word]+1
	return word_count	

def save_next_words(lines_arr):
	next_word_dict={}
	for i in xrange(len(lines_arr)):
		if lines_arr[i] not in next_word_dict.keys():
			next_word_dict[lines_arr[i]] = []
		if i < len(lines_arr)-1:
			next_word_dict[lines_arr[i]].append(lines_arr[i+1])
	return next_word_dict

def main():
	f=open(sys.argv[1],'r')
	text=f.read()
	lines_arr=text.split()
	#to get the word count in the file
	word_count_dict=get_word_count(lines_arr)
	random_word = random.choice(word_count_dict.keys())
	print random_word
	mimic= save_next_words(lines_arr)[random_word]
	s=' '
	print s.join(mimic)

if __name__ == '__main__':
	main()
