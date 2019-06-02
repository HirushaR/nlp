from nltk.corpus import wordnet

sa1 = wordnet.synsets('cake')
sa2 = wordnet.synsets('loaf')
sa3 = wordnet.synsets('bread')
cake = sa1[0]
loafb = sa2[0]
loaf = sa2[1]
bread =sa3[0]

# wu - palmer similarity
#print(bread.wup_similarity(cake))
#print(loaf.hypernyms())

ref = loaf.hypernyms()[0]
print(ref)
print(loaf.shortest_path_distance(ref))