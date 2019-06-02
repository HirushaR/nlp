from nltk.corpus import  webtext
from nltk.metrics import BigramAssocMeasures
from  nltk.collocations import BigramCollocationFinder
from nltk.corpus import stopwords

textWord = [w.lower() for w in webtext.words('pirates.txt')]
finder = BigramCollocationFinder.from_words(textWord)
#print(finder.nbest(BigramAssocMeasures.likelihood_ratio,10))
ignored_word = set(stopwords.words('english'))
print(ignored_word)
filterStpos = lambda w: len(w) <3 or w in ignored_word

finder.apply_word_filter(filterStpos)
print(finder.nbest(BigramAssocMeasures.likelihood_ratio,10))


