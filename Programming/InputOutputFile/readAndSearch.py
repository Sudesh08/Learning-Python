# # Read a file name is poem.txt and check weather twinkle word is present or not
#
# with open("poem.txt") as file:
#     content=file.read()
#     print(content)
#
# if "twinkle" in content.lower():
#     print("Twinkle world is present")
# else:
#     print("Twinkle world is not present")


found = False
with open("poem.txt", "r") as file:
    for line in file:
        print(line)
        if "twinkle" in line.lower():
            found = True
            print("The word 'twinkle' is present in the file.")
            break  # Stop reading the file after the first match

if not found:
    print("The word 'twinkle' is NOT present in the file.")
