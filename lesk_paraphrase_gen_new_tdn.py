from nltk.wsd import lesk
import re
from nltk.corpus import stopwords
import string
# from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
from nltk.corpus import wordnet as wn
from nltk import pos_tag

stop_words = set(stopwords.words('english'))
file = open('title+desc+nar.EXAMPLE', 'r').read()
array = re.split('<text>|</text>', file)
f1 = open("para_title+desc+nar.EXAMPLE", "w")
translator = str.maketrans(string.punctuation,
                           ' ' * len(string.punctuation))  # how to delete punctuation and put space instead
f1.write(
    "<parameters>\n<index>/home/ster/Desktop/example</index>\n<rule>method:dirichlet,mu:1000</rule>\n<count>1000</count>\n<trecFormat>true</trecFormat>\n")
k = 301
for i in range(len(array)):

    if (i % 2 == 1):
        f1.write("<query><type>indri</type><number>")
        f1.write(str(k))
        k = k + 1
        f1.write("</number> ")
        f1.write("<text>")
        sent = array[i].split("\n")
        #print(sent)

        for i in sent:
            # Word tokenizers is used to find the words
            # and punctuation in a string
            wordsList = nltk.word_tokenize(i)

            # removing stop words from wordList
            wordsList = [w for w in wordsList if not w in stop_words] #delete stop words for better metrics

            synsets = [lesk(sent, w) for w in wordsList]
            # print(synsets)
        for ws in wordsList:
            count_l = 0
            if (lesk(sent, ws) is not None):
                c=wn.synset(lesk(sent, ws).name()).lemma_names()
                #print(ws)
                #print(c)
                f1.write(ws+' ')    
                for l in c:
                    if(l.lower() != ws.lower()):
                       if (count_l < 1):
                            f1.write(l.translate(translator)+' ')
                            count_l=1
        f1.write("</text></query>\n")
        #print(wordsList)
        #print(list)
f1.write("</parameters>")
f1.close()
