from nltk.wsd import lesk
import re
from nltk.corpus import stopwords
import string
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
from nltk import pos_tag

stop_words = set(stopwords.words('english'))
file = open('title+desc.EXAMPLE', 'r').read()
array = re.split('<text>|</text>', file)
f1 = open("para_title+desc.EXAMPLE", "w")
translator = str.maketrans(string.punctuation,' ' * len(string.punctuation))  # how to delete punctuation and put space instead
f1.write(
    "<parameters>\n<index>/home/stelios/Desktop/IR-2019-2020-Project-1/indices/example</index>\n<rule>method:dirichlet,mu:1000</rule>\n<count>1000</count>\n<trecFormat>true</trecFormat>\n")
k = 301
count = 0;
for i in range(len(array)):

    if (i % 2 == 1):
        f1.write("<query><type>indri</type><number>")
        f1.write(str(k))
        k = k + 1
        f1.write("</number> ")
        f1.write("<text>")
        sent = array[i].split("\n")
        # print(sent)

        for i in sent:
            # Word tokenizers is used to find the words
            # and punctuation in a string
            wordsList = nltk.word_tokenize(i)

            # removing stop words from wordList
            # wordsList = [w for w in wordsList if not w in stop_words] #delete stop words for better metrics

            tagged = nltk.pos_tag(wordsList)
            # print(wordsList)
            
        synsets = [lesk(sent, w) for w in wordsList]
        # print(synsets)
        list = []
        for ws in wordsList:
            count = 0
            for ss in [n for synset in wn.synsets(ws) for n in synset.lemma_names()]:
                if(ss.lower()!= ws.lower()):
                    if(count<1):
                        list.append(ss)
                        count = 1
        print(list)

f1.close()









