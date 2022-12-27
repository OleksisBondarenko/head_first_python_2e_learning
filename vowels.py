vowels = ["a", "o", "u", "i", "e"]
word = "Hello world"
found = []

for letter in word: 
  is_letter_vowel = letter in vowels
  is_new_letter = letter not in found

  if is_letter_vowel and is_new_letter:
    found.append(letter)
 
for letter in found:
  print(letter)