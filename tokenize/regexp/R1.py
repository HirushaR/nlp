#helper class
from nltk.tokenize import regexp_tokenize
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer

sent1 = "i can't do this. I won't do that"
#print(word_tokenize(sent1))
#print(regexp_tokenize(sent1,"[\w']+"))

tok = RegexpTokenizer("[\w']+")
print(tok.tokenize(sent1))