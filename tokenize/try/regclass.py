#you have to add this file into library ,site-packages folder
#after you add you can use this file as a class

import re;
givenpatterns = [(r'won\'t', 'will not'),
                 (r'\'s', ' is'),
                 (r'\'d', 'would'),
                 (r'don\'t', 'do not')]

class RegexpReplacer(object):
    def __init__(self):
        self.patterns = givenpatterns

    def replace(self,text):
        for(raw, rep) in self.patterns:
            regex = re.compile(raw)
            text = regex.sub(rep, text)
        print(text)