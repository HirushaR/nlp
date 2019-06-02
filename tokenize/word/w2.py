from nltk.tokenize import word_tokenize
from nltk.tokenize import TreebankWordTokenizer
from nltk.tokenize import WordPunctTokenizer


tok2 = TreebankWordTokenizer()
tok3 = WordPunctTokenizer()

sent1 = "Hi my name is hirusha"
print(word_tokenize(sent1))

print(tok2.tokenize(sent1))
print(tok3.tokenize(sent1))

sent2 = "i won't let you bring cake"
print(word_tokenize(sent2))
print(tok2.tokenize(sent2))
print(tok3.tokenize(sent2))


