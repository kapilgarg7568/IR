from util import *

# Add your import statements here
from nltk.tokenize import TreebankWordTokenizer

class Tokenization():

	def naive(self, text):
		"""
		Tokenization using a Naive Approach

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""
		tokenizedText = []
		# Naive approach: tob bottom approach
		for i in text:
                        t = i.split(' ')
                        tokenizedText.append(t)
		return tokenizedText

	def pennTreeBank(self, text):
		"""
		Tokenization using the Penn Tree Bank Tokenizer

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""
		# Penn Tree Bank Tokenizer: tob bottom approach, uses Regex expression
		tokenizedText = []
		tokenizer = TreebankWordTokenizer()
		for i in text:
                        t = tokenizer.tokenize(i)
                        tokenizedText.append(t)
		return tokenizedText
