from . import Util_Classes
from word2number import w2n

def find_compound_dependencies(m,full_domain):   
    for x in m.children:
        if(x.dep_=="compound"):
            full_domain =  x.text + " " + full_domain
            return find_compound_dependencies(x,full_domain)
    return full_domain

def get_data_from_string(doc,results):
    values = []
    labels = []
    tups = []
    domain = results[0][0]
    for i in doc.ents:
        if i.label_ == "GPE":
            subject = i
    for i in results:
        if len(i[2]) <= 4:
            labels.append(i[2])
        else:
            values.append(i[2])
    for i in range(len(labels)):
        tuples = Util_Classes.plotTuple()
        tuples.domain = domain
        tuples.attribute = domain
        tuples.subject = subject.text
        tuples.date = labels[i]
        tuples.value = values[i]
        tups.append(tuples)
    return tups 

def get_number(string):
    if len(string.split()) > 1:
        try:
            val = w2n.word_to_num(string) * float(string.split()[0])
        except:
                return w2n.word_to_num(string)
        return val
    else:
        if "%" in string:
            return string.split("%")[0]
        try:
            return w2n.word_to_num(string)
        except:
            return float(string)