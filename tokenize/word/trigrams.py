from nltk.collocations import TrigramCollocationFinder
from nltk.metrics import TrigramAssocMeasures
from nltk.corpus import webtext
from nltk.corpus import stopwords

textword = [w.lower() for w in webtext.words('grail.txt')]
finder = TrigramCollocationFinder.from_words(textword)
#print(finder.nbest(TrigramAssocMeasures.likelihood_ratio,10))

ignored_words =set(stopwords.words('english'))
filterStop = lambda w: len(w) < 3 or w in ignored_words

finder.apply_word_filter(filterStop)
# print(finder.nbest(TrigramAssocMeasures.likelihood_ratio,10))
finder.apply_freq_filter(3)
print(finder.nbest(TrigramAssocMeasures.likelihood_ratio,30))
