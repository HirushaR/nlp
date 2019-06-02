# use nltk separate the sentences
from nltk.tokenize import sent_tokenize
parag = "My name is roky . i like nltk . i like python"
print(sent_tokenize(parag))
myArr = sent_tokenize(parag)
print(myArr)
print(myArr[2])