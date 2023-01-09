vowels_letters = ["a", "o", "u", "e", "i"]
vowels_frequency = {}

# word = input("Type word for search: ")
word = "hello world"

for char in word: 
  if char in vowels_letters:
    vowels_frequency.setdefault(char, 0) 
    # previous line equals:
    #  
    ### if char not it vowels_letters:
    ###     vowels_frequency[char] = 0

    vowels_frequency[char] += 1

for key, value in sorted(vowels_frequency.items()):
  print("Letter {key} was found {value} time(s)".format(key = key, value = value))