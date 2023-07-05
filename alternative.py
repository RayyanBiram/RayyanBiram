text = "Hello World"
#Defining the variable as an empty string
result = ""

#Loop through each character in the string
for i in range(len(text)):
    #Check if the index is even or odd
    if i % 2 == 0:
        #If the index is even, convert the character to lowercase and add it to the result string
        result += text[i].lower()
    else:
        #If the index is odd, convert the character to uppercase and add it to the result string
        result += text[i].upper()

print(result)

text = "I am learning to code"
words = text.split()

#Loop through each word in the string
for i in range(len(words)):
    #Check if the index is even or odd
    if i % 2 == 0:
        #If the index is even, convert the word to lowercase
        words[i] = words[i].lower()
    else:
        #If the index is odd, convert the word to uppercase
        words[i] = words[i].upper()

#Join the modified words back into a string and print the result
result = " ".join(words)
print(result)



