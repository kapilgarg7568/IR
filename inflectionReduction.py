from util import *

# Add your import statements here
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
 
class InflectionReduction:

	def reduce(self, text):
		"""
		Stemming/Lemmatization

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of
			stemmed/lemmatized tokens representing a sentence
		"""
		# Lemmatizer 
		lemmatizer = WordNetLemmatizer()
		reducedText = []
		for i in text:
                        t = [lemmatizer.lemmatize(c) for c in i]
                        reducedText.append(t)
                # Stemming (Porter Stemmer)
                # ps = PorterStemmer()
                # reducedText = []
                # for i in text:
                #     t = [ps.stem(c) for c in i]
                #     reducedText.append(t)
        
		return reducedText


