from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

ensw = stopwords.words('english')
#print(ensw)
parag1 = "what are you doing exactly right now? I want to get to my office."

paragArr = word_tokenize(parag1.lower())#lower() to convert all thing to lower case
print(paragArr)

filterArr = [item for item in paragArr if item not in ensw]
print(filterArr)