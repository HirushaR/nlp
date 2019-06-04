#TODO:learn regexp
import re;

regex = re.compile(r'don\'t')
fst  = "I don't go to school"
sst =regex.sub("do not",fst)
print(fst)
print(sst)
regex = re.compile(r'\'d')
fst1  = "He'd go to school"
sst1 =regex.sub("would",fst)
print(fst1)
print(sst1)

#TODO = create a oop class and try this
line = " I won't go there, He's a mad man.He won't end that. He'd have to go now."
givenpatterns = [(r'won\'t', 'will not'),
                 (r'\'s', ' is'),
                 (r'\'d', 'would'),
                 (r'don\'t', 'do not')]

def repalce(text, patterns):
    for(raw, rep) in patterns:
        regex1 = re.compile(raw)
        text = regex1.sub(rep, text)
    print(text)
repalce(line, givenpatterns)

