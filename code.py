words = []
with open("find_words.txt", "r") as fopen:
    for line in fopen:
        words.append(line.strip("\n"))
    
# print(words)


import csv
with open('french_dictionary.csv', mode='r') as inp:
    reader = csv.reader(inp)
    frenchWords = {rows[0]:rows[1] for rows in reader}

# print(frenchWords)
finalWords = []
for word in words:
    if word in frenchWords:
        finalWords.append(word)

# print(finalWords)
import re

header = ["English Word", "French Word", "Frequency"]
with open("t8.shakespeare.txt", "r+") as f:
    text = f.read()
    listOfWords = text.split()
    fcsv = open("frequency.csv","r+",encoding="UTF8")
    csvValues = fcsv.read()
    writer = csv.writer(fcsv)
    writer.writerow(header)
    for word in listOfWords:
        value = []
        if word.lower() in finalWords:

            value = [word, frenchWords[word.lower()],text.count(word)]
            if value[0] not in csvValues:
                writer.writerow(value) 
            text = re.sub(word,frenchWords[word.lower()],text)
        else:
            continue
        f.seek(0)
        f.write(text)
        f.truncate()
    fcsv.close()