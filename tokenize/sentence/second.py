from nltk.tokenize import sent_tokenize
import nltk.data
tokernizer = nltk.data.load('tokenizers/punkt/english.pickle')
parag = "i like crayons. i fly high. i love you "
print(tokernizer.tokenize(parag))
arrt = tokernizer.tokenize(parag)
print(arrt[2])