## AUTOMATIC READING COMPREHENSION 2.0 BY Fiji370, BUILT ON 2/22/17 ##


## Imports
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk import ne_chunk
from nltk import pos_tag
from nltk import sent_tokenize

## Read the input document
with open("INPUT.txt") as text:
    inputDoc = text.read()

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
    namedEntities = []
    
    together = []
    
    smartKeys = keywords
    
    firstMatches = [i for i in sent_tokenize(document) for x in word_tokenize(i) if x in smartKeys]
    
    
    for i in firstMatches:
        for x in ne_chunk(pos_tag(word_tokenize(i))):
            try:
               namedEntities.append(x.leaves())
            except:
                continue
    
    for i in namedEntities:
        transientList = []
        for x in i:
            transientList.append(x[0])
        together.append(transientList)
    
    together = [" ".join(i) for i in together]
    nouns = together
    
    for i in firstMatches:
        for x in pos_tag(word_tokenize(i)):
            if "NN" in x[1] and x[0] not in " ".join(nouns):
                nouns.append(x[0])
    
    for i in nouns:
        smartKeys.append(i)
    
    smartKeys = [i for i in smartKeys if i.lower() not in set(stopwords.words('english')) and word_tokenize(document).count(i.lower()) < 50]
    smartKeys = set(smartKeys)
    smartKeys = list(smartKeys)
    
    return smartKeys

def presentable(snippet):
    pass

print matchSnippets(inputDoc, preprocess(litQ))