listOfWord=["donkey","Gadha","Lalchi","Pagal"]

with open("donkeyfile.txt","r",encoding="utf-8") as file:
    word=file.read()
    print(word)

for badWord in listOfWord:
    print(badWord, "line")
    word = word.replace(badWord, "#" * len(badWord))

with open("donkeyfile.txt","w",encoding="utf-8") as file:
    file.write(word)