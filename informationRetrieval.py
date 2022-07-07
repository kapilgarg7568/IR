from util import *

# Add your import statements here
import numpy as np

class InformationRetrieval():

	def __init__(self):
		self.index = None

	def buildIndex(self, docs, docIDs):
		"""
		Builds the document index in terms of the document
		IDs and stores it in the 'index' class variable

		Parameters
		----------
		arg1 : list
			A list of lists of lists where each sub-list is
			a document and each sub-sub-list is a sentence of the document
		arg2 : list
			A list of integers denoting IDs of the documents
		Returns
		-------
		None
		"""

		#Fill in code here

		index = docIDs
		self.index = index
		self.docs = docs


	def rank(self, queries):
		"""
		Rank the documents according to relevance for each query

		Parameters
		----------
		arg1 : list
			A list of lists of lists where each sub-list is a query and
			each sub-sub-list is a sentence of the query
		

		Returns
		-------
		list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		"""

		doc_IDs_ordered = []

		#Fill in code here
		unique_w = []
		unique_w_doc = [[]]*len(self.index)
		unique_w_q = [[]]*len(queries)
		vec_q = [0]*len(queries)
		vec_doc = [0]*len(self.index)
		for i in self.index:
			for s in self.docs[i-1]:
				for w in s:
					if w not in unique_w:
						unique_w.append(w)
					if w not in unique_w_doc[i-1]:
						unique_w_doc[i-1].append(w)
		idf_w = [0]*len(unique_w)
		tf_w_doc = [0]*len(self.index)
		for i in self.index:
			tf_w_doc[i-1] = [0]*len(unique_w)
			for s in self.docs[i-1]:
				for w in s:
					tf_w_doc[i-1][unique_w.index(w)] += 1
		tf_w_doc = np.array(tf_w_doc)
		for k in range(len(unique_w)):
			idf_w[k] += np.count_nonzero(tf_w_doc[:,k])
		tf_w_q = [0]*len(queries)
		for i in range(len(queries)):
			tf_w_q[i] = [0]*len(unique_w)
			for s in queries[i]:
				for w in s:
					if w in unique_w:
						tf_w_q[i][unique_w.index(w)] += 1
		vec_doc = (np.log10(len(self.index))- np.log10(np.array(idf_w)))*tf_w_doc
		vec_doc = vec_doc+0.00001
		vec_doc = vec_doc/np.linalg.norm(vec_doc, ord=2, axis=1, keepdims=True)
		vec_q = (np.log10(len(self.index))- np.log10(np.array(idf_w)))*np.array(tf_w_q)
		for i in range(len(queries)):
			rank = np.zeros((len(self.index),2))
			rank[:,0] = np.arange(len(self.index))
			rank[:,1] = -np.dot(vec_doc,vec_q[i])/(np.linalg.norm(vec_q[i]))
			rank = rank[rank[:,1].argsort()]
			doc_IDs_ordered.append(rank[:,0]+1)

		return doc_IDs_ordered




