import re
import string

#merge the files at ubuntu with command "cat file1 file2 file3 >> final_file"
x=open("merged.trec6","r").read()
f1=open("title+desc.EXAMPLE","w")

array = re.split('<top>\n|\n</top>\n\n',x)
translator = str.maketrans(string.punctuation, ' '*len(string.punctuation))#how to delete punctuation and put space instead
f1.write("<parameters>\n<index>/home/stelios/Desktop/IR-2019-2020-Project-1/indices/example</index>\n<rule>method:dirichlet,mu:1000</rule>\n<count>1000</count>\n<trecFormat>true</trecFormat>\n")
for i in range(len(array)):
    cut = re.split('<num> Number: |\n<title> |\n\n<desc> Description:|\n<narr> Narrative: ',array[i])
    for j in cut[1:4]:
        if (cut[1] == j):
            f1.write("<query><type>indri</type><number>")
            f1.write(j.translate(translator))
            f1.write("</number> ")
            f1.write("<text>")
        elif (cut[2]==j):
            f1.write(j.translate(translator))

        else:
            cut2= re.split("\n",j)
            for k in range(len(cut2)):
                f1.write(cut2[k].translate(translator)+" ")
    for j in cut[2:3]:
        f1.write("</text></query>\n")
f1.write("</parameters>")
f1.close()