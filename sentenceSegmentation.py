from util import *

# Add your import statements here
import nltk.data

class SentenceSegmentation():

	def naive(self, text):
		"""
		Sentence Segmentation using a Naive Approach

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each string is a single sentence
		"""
		# Naive approach for sentence tokenization: Top down approach
		segmentedText = text.split('.')

		return segmentedText

	def punkt(self, text):
		"""
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each strin is a single sentence
		"""
		# Punkt Tokenizer: Bottom up approach
		tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
		segmentedText = tokenizer.tokenize(text)

		return segmentedText
		
		return segmentedText
