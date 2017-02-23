## AUTOMATIC READING COMPREHENSION 2.0 BY Fiji370, BUILT ON 2/22/17 ##


## Imports
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk import ne_chunk
from nltk import pos_tag

## Ask for the question
litQ = raw_input("Please input your question: \n")

## Extracts useful information for matching. Nouns, named entities, and verbs will be collected.
def preprocess(question):
    ## NER and noun extraction
    namedEntities = []
    nouns = []
    together = []
    
    meaningless = set(stopwords.words('english'))
    
    cleanedQuestion = [i for i in word_tokenize(question) if i not in meaningless]
    
    for i in ne_chunk(pos_tag(cleanedQuestion)):
        try:
            namedEntities.append(i.leaves())
        except:
            continue
    
    for i in namedEntities:
        transientList = []
        for x in i:
            transientList.append(x[0])
        together.append(transientList)
    together = [" ".join(i) for i in together]
    nouns = together
    
    remaining = [i for i in cleanedQuestion if i not in " ".join(nouns)]
    
    for i in pos_tag(remaining):
        if "NN" in i[1]:
            nouns.append(i[0])
            
    nouns = set(nouns)
    nouns = list(nouns)
    
    ## Verb extraction
    verbs = [i[0] for i in pos_tag(cleanedQuestion) if "VB" in i[1]]
    
    ## Return everything
    both = []
    for i in nouns:
        both.append(i)
    for i in verbs:
        both.append(i)
        
    return both

def matchSnippets(document, keywords):
    pass

def presentable(snippet):
    pass
    
print(preprocess(litQ))