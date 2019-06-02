from nltk.corpus import wordnet

word1 = "weapon"
synArr = wordnet.synsets(word1)
print(synArr)
# for i in range(len(synArr)):
#     print(i+1)
#     woi = synArr[i]
#     print(woi)
#     print(woi.definition())
#     print("---------------")
woi = synArr[0]
print(woi)
print(woi.definition())
print(woi.name())
print(woi.pos())
print(woi.hypernyms())

woi2 = woi.hyponyms()[1]
print(woi2)
print(woi2.definition())

