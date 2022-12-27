vowels = ["a", "o", "u", "e", "i"]
word = input("Type word for search\n")

found_letters = []
for letter in word:
  if letter in vowels:
    if letter not in found_letters:
      found_letters.append(letter)
    
print("Found next vowel letters")
for letter in found_letters: 
  print(letter)

