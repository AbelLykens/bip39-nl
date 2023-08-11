#!/usr/bin/env python3
import sqlite3
import os
import re


con = sqlite3.connect("/dev/shm/words-nl.db")
cur = con.cursor()

# Table
#cur.execute("DROP table words")
cur.execute("CREATE TABLE IF NOT EXISTS words (source, word);")

# Source files
dir_list = os.listdir('source/xml')
num_files = len(dir_list)
data = []
i=0

# Seen
cur.execute("SELECT source FROM words GROUP BY source")
resdata=cur.fetchall()
sources = []
for source in resdata:
    sources.append(source)

for xmlfile in dir_list:
    i+=1

    path = f"source/xml/{xmlfile}"


    # Did we parse this already?
    if path in sources:
        print(f"I {i}/{num_files}")
        continue
    else:
        print(f"P {i}/{num_files}")

    # Import
    with open(f"source/xml/{xmlfile}",'r') as f:
        content = f.read()
        #print(content)
        words = re.findall("<w[^>]*>([a-z]{4,8})</w>",content)
        for word in words:
            data.append( (path,word.lower()) )

    if i % 1000 == 0:
        cur.executemany("INSERT INTO words VALUES(?, ?)", data)
        con.commit()
        data = []

cur.executemany("INSERT INTO words VALUES(?, ?)", data)
con.commit()

cur.execute("select count(word) num,word from words group by word HAVING num > 5 ORDER BY num DESC;")
with open("result.csv","w") as output:
    for res in cur.fetchall():
        line = f"{res[1]}"
        print(line)
        output.write(line + "\n")
        
