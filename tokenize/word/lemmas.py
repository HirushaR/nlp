from nltk.corpus import wordnet

sArr = wordnet.synsets('win')    #Array of synset
woi = sArr[2]
#print(woi.lemmas())
#print(woi.lemmas()[0].name())
synArr = []                      #Array of synonyms
antArr = []
for syn in sArr:
    for lem in syn.lemmas():
        synArr.append(lem.name())
# print(len(synArr))
# print(len(set(synArr)))
print(woi.lemmas()[0].antonyms())
print(woi.lemmas()[0].antonyms()[0])
print(woi.lemmas()[0].antonyms()[0].name())


for syn in sArr:
    for lem in syn.lemmas():
        for ant in lem.antonyms():
            antArr.append(ant.name())


print(antArr)