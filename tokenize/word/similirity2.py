from nltk.corpus import wordnet

catArr = wordnet.synsets('cat')
dogArr = wordnet.synsets('dog')
doi = dogArr[0]
coi = catArr[0]
print(doi.wup_similarity(coi))
#leacock chodorow
print(doi.lch_similarity(coi))
print(coi.lch_similarity(doi))


