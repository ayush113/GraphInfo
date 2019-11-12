from .Utils.Util_Classes import *
from .Utils.preprocessor import *
from .Utils.Util_Functions import *
import spacy


def extract_tuples(inp):
	# Doc is the tokenized spacy document with all relationships
	root,verb_list,doc,sentence = preprocess(inp)
	verb = root
	verbs1 = [ "is" , "was" ,"were","are" , "been", "be"]
	verbs2 = ["has", "had", "have","having"]
	verbs3 = [""]
	aux_tups = []
	if len(verb_list) > 1:
		for ent in doc.ents:
	#         print(ent.text,ent.label_)
			#doc2 =  nlp(ent.text)
			if(ent.label_=="CARDINAL"):
				#Split the numbers and units
				ents = ent.text.split(' ')
				for i in range(len(ents)):
					try:
						ents[i] = w2n.word_to_num(ents[i])
					except:
						if(re.match(r"[-+]?\d*\.\d+|\d+", ents[i])):
							ents[i] = float(ents[i])
							sentence = sentence.replace(ent.text,str(ents[i]*int(w2n.word_to_num(ents[i+1]))))
						else:
							ents[i] = ents[i]
							break
		nlp = spacy.load("en")
		doc = nlp(sentence)
		for i in doc:
			if(i.dep_=="prep"):
				for j in i.children:
					if(j.dep_=="pobj" or j.dep_=="dobj"):
						print(i.head.text,i.text,j.text)
						aux_tups.append(Rels(i.head.text,i.text,j.text))
						if(i.text=="between"):
							for m in j.children:
								if(m.dep_=="conj"):
									print(m.text)
	else:
		if(verb.text in verbs1):
			tuples = plotTuple()
			print("Case 1")
			for i in verb.children:
				if(i.dep_=="nsubj" and (i.pos_ == "NOUN" or i.pos_ == "PROPN")):
					print(i.text)
		#             print(find_compound_dependencies(i,i.text))
					if i.pos_ == "PROPN":
						tuples.subject = i.text
					else:
						tuples.domain = i.text
						tuples.attribute = find_compound_dependencies(i,i.text)
					for j in i.children:
						if (j.dep_ == "poss" and (j.pos_=="PROPN" or j.pos_=="NOUN" or j.pos_=="PRON")):
							print(j.text)
							tuples.subject = j.text
						if(j.dep_ == "prep" and (j.text=="of" or j.text=="for") and j.pos_=="ADP"):
							print(j.text)
							print(find_compound_dependencies(j,j.text))
							for m in j.children:
								if(m.dep_ == "pobj" and (m.pos_ == "NOUN" or m.pos_ == "PROPN" or m.pos_ == "PRON")):
									print(i.text,j.text,m.text)
									print(find_compound_dependencies(m,m.text))
									tuples.subject = m.text
									break
							break
					for j in verb.children:
						if(j.dep_ == "attr"):
							print(j.text)
							#print(find_compound_dependencies(j,j.text))
							if j.text == "%":
								for k in j.children:
									if k.pos_ == "NUM":
										print(k.text)
										tuples.value = k.text+j.text
							else:
								tuples.value = find_compound_dependencies(j,j.text)
							break
				if(i.dep_ == "nsubj" and (i.pos_ == "NOUN" or i.pos_ == "PROPN" or i.pos_=="PRON")):
					for j in i.children:
						if(j.dep_=="acomp" and (j.pos_ == "ADJ" or j.pos_ == "ADV")):
							for k in j.children:
								if(k.dep_ == "npadvmod"):
									print(k.text,j.text,i.text)
									break
							break
		elif(verb.text in verbs2):
			tuples = plotTuple()
			print("Case 2")
			for i in verb.children:
				if(i.dep_=="dobj" and (i.pos_=="NOUN" or i.pos_=="PROPN")):
					if i.pos_ == "NOUN":
						tuples.domain = i.text
						tuples.attribute = find_compound_dependencies(i,i.text)
					for j in i.children:
						if(j.dep_=="prep" and j.pos_=="ADP"):
							print(j.text)
							print(find_compound_dependencies(j,j.text))
							for m in j.children:
								if(m.dep_=="pobj"):
									print(m.text,j.text,i.text)
									tuples.value = find_compound_dependencies(m,m.text)
									break
							break
					for j in verb.children:
						if(j.dep_=="nsubj" and (j.pos_ == "NOUN" or j.pos_ == "PROPN" or j.pos_=="PRON")):
							print(j.text)
							if j.pos_ == "PROPN":
								tuples.subject = j.text
				elif(i.dep_=="nsubj" and (i.pos_=="NOUN" or i.pos_=="PROPN" or i.pos_=="PRON")):
					if i.pos_ == "PROPN":
						tuples.subject = i.text
					for j in i.children:
						if(j.dep_=="dobj"):
							tuples.domain = j.text
							tuples.attribute = find_compound_dependencies(j,j.text)
							for m in j.children:
								if(m.text=="of" and m.dep_=="prep" and m.pos_=="ADP"):
									tuples.value = m.text
									print(m.text,j.text,i.text)
									break
							break
		else:
			print("Case 3")
			tuples = plotTuple()
			for i in verb.children:
				if(i.dep_=="attr" or i.dep_=="acomp"):
					for j in verb.children:
						if(j.dep_=="nsubj" and (j.pos_ == "NOUN" or j.pos_ == "PROPN" or j.pos_=="PRON")):
							for m in j.children:
								if(m.dep_=="poss" and (m.pos_=="PROPN" or m.pos_=="NOUN")):
									print(m.text,j.text.i.text)
									break
							break
					break
				if(i.dep_=="auxpass" and i.text in verbs1):
					for j in verb.children:
						if(j.dep_=="nsubjpass" and (j.pos_ == "NOUN" or j.pos_ == "PROPN" or j.pos_=="PRON")):
							for m in verb.children:
								if(m.dep_=="prep" and m.pos_=="ADP"):
									for n in m.children:
										if(n.dep_=="pobjprint(find_compound_dependencies(i,i.text))"):
											print(n.text,m.text,j.text,i.text)
											break
									break
							break
					break
				if (i.dep_ =="nsubj") and (i.pos_ == "NOUN" or i.pos_ == "PROPN" or i.pos_ == "PRON"):
					print(i.text)
					tuples.domain = i.text
					for j in i.children:
						if j.dep_ == "poss" and (j.pos_ == "PROPN" or j.pos_ == "NOUN" or j.pos_ == "PRON"):
							print(j.text)
							tuples.subject = j.text
							break
					for j in verb.children:
						if (j.dep_ == "dobj") and j.pos_ == "NUM":
							print(find_compound_dependencies(j,j.text))
							tuples.value = find_compound_dependencies(j,j.text)
					break
	if len(aux_tups) != 0:
		res = [i.get_res() for i in aux_tups]

	final_results = []

	if len(verb_list) > 1:
		tuples = get_data_from_string(doc,res)
		for i in tuples:
			final_results.append(i.get_tuple())
	else:
		#work with normal tuple
		final_results.append(tuples.get_tuple())
	print(final_results)
	return final_results