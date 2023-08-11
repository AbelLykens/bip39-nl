#!/usr/bin/env python3

seenfirst4 = []
goodwords = []

with open('source/opentaal.csv','r') as opentaal:
    for line in opentaal:
        goodwords.append(line.rstrip())

with open('result_uniquefirst4.csv','w') as resfile:
    with open('result.csv') as openfile:
        for line in openfile:
            word = line.rstrip()
            first4 = word[0:4]
    
            if first4 in seenfirst4:
                continue
            if word not in goodwords:
                continue
        
            seenfirst4.append(first4)
            print(word)
            resfile.write(word+"\n")
        
