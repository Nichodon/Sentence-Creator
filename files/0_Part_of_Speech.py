import urllib.request, re #import needed modules for python3
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

def pos(word): #word you want to search for
    url="https://en.oxforddictionaries.com/definition/" #link
    url=url+word #concatenate url and word to form the final url
    text=urllib.request.urlopen(url).read().decode('utf-8') #open the url, read it and change the encoding to utf-8. Needed to use regex on it
    found = re.findall('<h3 class="ps pos"><span class="pos">(.+?)</span></h3>' , text)
    poss=set()
    for i in found:
        poss.update(set(i.split('<span class="listSeparator">&amp;</span>')))
    if len(poss)>0:
        return ''.join((','+','.join(poss)).split()) #regex finds all occurences of the specific
    else:
        return '!!!'

fname = input("letter:")

file = []

with open(dir_path+"/"+fname+".txt", "r") as f:
    file = f.read().splitlines()
    for i in range(0,len(file)):
        line = file[i]
        if line[0] is not " " and "," not in line: # If line unmodified and is a single word
            line=line.replace("!","")+pos(line)
            file[i]=line
            print(line)
with open(dir_path+"/"+fname+".txt", "w") as f:
    for line in file:
        f.write(line+"\n")
