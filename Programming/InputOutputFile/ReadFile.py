# Read The file where file name is dummyFile.txt

f=open("dummyFile.txt","r")
text =f.read()
print(text)
f.close()