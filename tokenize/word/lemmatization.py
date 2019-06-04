from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer

lzr = WordNetLemmatizer()
print(lzr.lemmatize('dancing',pos = 'v'))
print(lzr.lemmatize('working',pos='a'))
stm = PorterStemmer()
print(stm.stem('dancing'))
print(stm.stem('believes'))
print(lzr.lemmatize('believes'))
print(stm.stem('buses'))
#TODO:stem is like clear last word
print(lzr.lemmatize('buses'))