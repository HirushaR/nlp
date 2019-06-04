from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import RegexpStemmer

#snowballStemmert - languages other than english

pstemmer = PorterStemmer()
print(pstemmer.stem('dancing'))
print(pstemmer.stem('dancer'))
print(pstemmer.stem('cooking'))
print(pstemmer.stem('cookery'))
#PoterStemmer ->least aggressinve
lstemmer = LancasterStemmer()
print(lstemmer.stem('dancing'))
print(lstemmer.stem('cookery'))
#regexp
rstemer = RegexpStemmer('ing')
print(rstemer.stem('dancing'))

