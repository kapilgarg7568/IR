from util import *

# Add your import statements here
from nltk.corpus import stopwords

class StopwordRemoval():

	def fromList(self, text):
		"""
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence with stopwords removed
		"""
		# Storing all the stop words from the nltk corpus
		# top bottom approach
		stop_words = set(stopwords.words('english'))
		stopwordRemovedText = []
		for i in text:
                        t = [c for c in i if not c in stop_words]
                        stopwordRemovedText.append(t)
        
		return stopwordRemovedText




	
