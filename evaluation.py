from util import *

# Add your import statements here
import numpy as np


class Evaluation():

	def queryPrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of precision of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The precision value as a number between 0 and 1
		"""

		precision = -1

		#Fill in code here
		qp = 0
		for i in range(k):
			if query_doc_IDs_ordered[i] in true_doc_IDs:
				qp += 1
		precision = qp/k
		return precision


	def meanPrecision(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of precision of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean precision value as a number between 0 and 1
		"""

		meanPrecision = -1

		#Fill in code here
		relevant_doc = []
		for i in range(len(query_ids)):
			d = []
			for j in range(len(qrels)):
				if int(qrels[j]["query_num"]) == query_ids[i]:
					d.append(int(qrels[j]["id"]))
			relevant_doc.append(d)
		mp = 0
		for i in range(len(query_ids)):
			mp += self.queryPrecision(doc_IDs_ordered[i], query_ids[i], relevant_doc[i], k)
		meanPrecision = mp/len(query_ids)
		return meanPrecision

	
	def queryRecall(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of recall of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The recall value as a number between 0 and 1
		"""

		recall = -1

		#Fill in code here
		qr = 0
		for i in range(k):
			if query_doc_IDs_ordered[i] in true_doc_IDs:
				qr+=1
		recall = qr/len(true_doc_IDs)
		return recall


	def meanRecall(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of recall of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean recall value as a number between 0 and 1
		"""

		meanRecall = -1

		#Fill in code here
		rel_doc = []
		for i in query_ids:
			d = []
			for j in range(len(qrels)):
				if int(qrels[j]["query_num"]) == i:
					d.append(int(qrels[j]["id"]))
			rel_doc.append(d)
		mr = 0
		for i in range(len(query_ids)):
			mr += self.queryRecall(doc_IDs_ordered[i], query_ids[i], rel_doc[i], k)
		meanRecall = mr/len(query_ids)
		return meanRecall


	def queryFscore(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of fscore of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The fscore value as a number between 0 and 1
		"""

		fscore = -1

		#Fill in code here
		if self.queryPrecision(query_doc_IDs_ordered, query_id, true_doc_IDs, k) == 0 or self.queryRecall(query_doc_IDs_ordered, query_id, true_doc_IDs, k) ==0:
			fscore = 0
		else:
			fscore = 2/((1/self.queryPrecision(query_doc_IDs_ordered, query_id, true_doc_IDs, k)) + (1/self.queryRecall(query_doc_IDs_ordered, query_id, true_doc_IDs, k)))
		return fscore


	def meanFscore(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of fscore of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value
		
		Returns
		-------
		float
			The mean fscore value as a number between 0 and 1
		"""

		meanFscore = -1

		#Fill in code here
		rel_doc = []
		for i in range(len(query_ids)):
			d = []
			for j in range(len(qrels)):
				if int(qrels[j]["query_num"]) == int(query_ids[i]):
					d.append(int(qrels[j]["id"]))
			rel_doc.append(d)
		mf = 0
		for i in range(len(query_ids)):
			mf += self.queryFscore(doc_IDs_ordered[i], query_ids[i], rel_doc[i], k)
		meanFscore = mf/len(query_ids)
		return meanFscore
	

	def queryNDCG(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of nDCG of the Information Retrieval System
		at given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The nDCG value as a number between 0 and 1
		"""

		nDCG = -1

		#Fill in code here
		if query_doc_IDs_ordered[0] in true_doc_IDs:
			n = true_doc_IDs[query_doc_IDs_ordered[0]]
		else:
			n = 0
		for i in range(1,k):
			if query_doc_IDs_ordered[i] in true_doc_IDs:
				n += true_doc_IDs[query_doc_IDs_ordered[i]]/(np.log(i+1)/np.log(2))
		d = list(true_doc_IDs.keys())
		true = np.zeros((len(d),2))
		true[:,0] = d
		for i in range(len(d)):
			true[i,1] = true_doc_IDs[d[i]]
		true = -true
		true = true[true[:,1].argsort()]
		true = -true
		ideal = true[0,1]
		for i in range(1,min(k,len(d))):
			ideal += true[i,1]*np.log(2)/np.log(i+1)
		nDCG = n/ideal
		#print(nDCG)
		return nDCG


	def meanNDCG(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of nDCG of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean nDCG value as a number between 0 and 1
		"""

		meanNDCG = -1

		#Fill in code here
		doc_rel = []
		for i in range(len(query_ids)):
			d = {}
			for j in range(len(qrels)):
				if int(qrels[j]['query_num']) == query_ids[i]:
					d[int(qrels[j]["id"])] = 5-int(qrels[j]["position"])
			doc_rel.append(d)
		#print(doc_rel)
		n = 0
		for i in range(len(query_ids)):
			n += self.queryNDCG(doc_IDs_ordered[i], query_ids[i],doc_rel[i], k)
		meanNDCG = n/len(query_ids)
		return meanNDCG


	def queryAveragePrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of average precision of the Information Retrieval System
		at a given value of k for a single query (the average of precision@i
		values for i such that the ith document is truly relevant)

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The average precision value as a number between 0 and 1
		"""

		avgPrecision = -1

		#Fill in code here
		rel = []
		s = 0
		for i in range(k):
			if int(query_doc_IDs_ordered[i]) in true_doc_IDs:
				s +=1
				rel.append(s)
			else:
				rel.append(0)
		a = 0
		#print(s)
		for i in range(k):
			a += rel[i]/(i+1)
		if a ==0:
			avgPrecision = 0
		else:
			rel = np.array(rel)
			avgPrecision = a/s
		return avgPrecision


	def meanAveragePrecision(self, doc_IDs_ordered, query_ids, q_rels, k):
		"""
		Computation of MAP of the Information Retrieval System
		at given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The MAP value as a number between 0 and 1
		"""

		meanAveragePrecision = -1

		#Fill in code here
		rel_doc = []
		for i in range(len(query_ids)):
			d = []
			for j in range(len(q_rels)):
				if int(q_rels[j]["query_num"]) == query_ids[i]:
					d.append(int(q_rels[j]["id"]))
			rel_doc.append(d)
		#print(rel_doc)
		mapn = 0
		for i in range(len(query_ids)):
			mapn += self.queryAveragePrecision(doc_IDs_ordered[i], query_ids[i], rel_doc[i], k)
		meanAveragePrecision = mapn/len(query_ids)
		return meanAveragePrecision

