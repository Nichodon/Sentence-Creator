from urllib2 import urlopen
import re
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

#word: word to search for
def pos(word):
    url = 'https://en.oxforddictionaries.com/definition/'
    #concat for final url, open url in utf-8
    url += word
    text = urlopen(url).read().decode('utf-8')
    found = re.findall(
        '<h3 class="ps pos"><span class="pos">(.+?)</span></h3>' , text)
    poss = set()
    for i in found:
        poss.update(set(i.split('<span class="listSeparator">&amp;</span>')))
    #regex finds all occurences
    return ''.join((','+','.join(poss)).split()) if len(poss) > 0 else '!!!'

fname = raw_input('Letter: ')

file = []

with open(dir_path + '/' + fname + '.txt', 'r') as f:
    file = f.read().splitlines()
    for i in range(0, len(file)):
        line = file[i]
        line = re.sub(r' ->(.+?)]', '', line)
        #if line not changed and is single word
        if line[0] is not ' ' and ',' not in line:
            line = line.replace('!', '')+pos(line)
            file[i] = line
            print(line)
with open(dir_path + '/' + fname + '.txt', 'w') as f:
    for line in file:
        f.write(line + '\n')
