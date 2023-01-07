# slices / зрізи

letters = "Dont panic!"
list_letter = letters[:: 1]
negative_list_letters = letters[::-1]

print(list_letter)
print("backward list", negative_list_letters )

print()

book = "The Hitchhiker's Guide to the Galaxy"
booklist = list(book)
print(booklist) 

print(booklist[0:3])
print(booklist[-6:])
print(booklist[-10: -7])

print(booklist[::-1])
print(booklist[::2])

print("word", ''.join(booklist[4:14]))
print("backward word", ''.join(booklist[13:3: -1]))