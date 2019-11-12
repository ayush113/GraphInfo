import spacy
from word2number import w2n
import re


def preprocess(data):
	nlp = spacy.load("en")
	sentence = data
	sentence = sentence.replace('per cent','%')
	sentence = sentence.replace('percent','%')
	doc = nlp(data)
	
	verb_list = []

	for token in doc:
	    if(token.dep_=="ROOT"):
	        #tree = replicateTree(token,None)
	        root = token
	    if token.pos_ == "VERB" or token.pos_ == "AUX":
	        verb_list.append(token)
	return root,verb_list,doc,sentence