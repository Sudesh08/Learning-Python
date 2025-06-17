listOfWord="Python"
with open("isPythonPresent.txt","r") as file:
    word=file.read()

    if listOfWord.lower() in word.lower():
        print("Python Present")
    else:
        print("Python is not present")