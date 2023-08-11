#!/usr/bin/env python3
import sqlite3
import os
import re


con = sqlite3.connect("words-nl.db")
cur = con.cursor()

# Table
cur.execute("DROP table words")
cur.execute("CREATE TABLE IF NOT EXISTS words (source, word);")

# Source files
dir_list = os.listdir('source/xml')
num_files = len(dir_list)
i=0

for xmlfile in dir_list:
    i+=1
    print(f"{i}/{num_files}")

    path = f"source/xml/{xmlfile}"
    with open(f"source/xml/{xmlfile}",'r') as f:
        content = f.read()
        #print(content)
        words = re.findall("<w[^>]*>([a-z]{4,8})</w>",content)
        data = []
        for word in words:
            data.append( (path,word.lower()) )

        cur.executemany("INSERT INTO words VALUES(?, ?)", data)
        con.commit()

cur.execute("select count(word) num,word from words group by word order by num DESC limit 10000;")
with open("result.csv","w") as output:
    for res in cur.fetchall():
        line = f"{res[1]}"
        print(line)
        output.write(line + "\n")
        
