with open("isPythonPresent.txt","r") as file:
    lines=file.readlines()
    print(lines)

lineno=1
for line in lines:
    if "python" in line:
        print(f"Python found in line no. {lineno}")
        break
    lineno += 1
else:
    print("Python not found in file")
