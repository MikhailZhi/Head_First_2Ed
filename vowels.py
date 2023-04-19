for num in 'Hello!':
    print (num)
print ()


vowels = ['a', 'e', 'i', 'o', 'u']
word_1 = input ('Provide a word to search for vowels: ')
found = []


for letter in word_1:
    if letter in vowels:
        if letter not in found:
            found.append (letter)


print ()
print (len(found))
print ()


for letter in found:
    print (letter)

print ()
print ("That's all!")
