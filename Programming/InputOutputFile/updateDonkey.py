
with open("donkeyfile.txt","r",encoding="utf-8") as file:
    word=file.read()

replaceWord=word.replace("donkey","######")
with open("donkeyfile.txt","w",encoding="utf-8") as file:
    file.write(replaceWord)

