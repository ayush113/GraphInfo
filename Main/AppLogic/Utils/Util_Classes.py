'''
Tree object class to hold all information from parse trees
'''
class TreeNode(object):
    def __init__(self, depLabel,text,posTag):
        self.depLabel = depLabel
        self.text = text
        self.posTag = posTag
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

'''
Format to store relations obtained from trees
'''
class Rels:
    def __init__(self, first, prep,second):
        self.first = first
        self.prep = prep
        self.second = second
    
    def get_res(self):
        return [self.first,self.prep,self.second]



'''
Intermediary Tuple form representation for plotting
'''
class plotTuple(object):
    def __init__(self, domain=None, attribute=None, subject=None, value=None, date=None):
        self.domain = domain
        self.attribute = attribute
        self.subject = subject
        self.value = value
        self.date = date
    
    def get_tuple(self):
        return [self.domain,self.attribute,self.subject,self.value,self.date]