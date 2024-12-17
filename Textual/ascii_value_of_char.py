print("Enter a String: ", end="")

# Input from user
text = input()

# Python function to get length of text variable's value
textlength = len(text)

# Iterate the characters
for char in text:
    ascii = ord(char)
    print(char, "\t", ascii)
