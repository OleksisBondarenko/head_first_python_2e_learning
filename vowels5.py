# The power of set |  Сила множин
# 
# set_a = {"a", "b", "c", "d" }
# set_b = { "a", "e", "i", "c" }
#
# TRUE POWER iS:
# 
# UNION set_a.union(set_b) "=" { "b", "c", "d", "a", "e", "i" }
#
# DIFFERENCE set_a.union(set_b) "=" { "b", "d" }
#
# INTERSECTION set_a.intersection(set_b) "=" { "a", "c" }
#
# TEST: 

# set_a = {"a", "b", "c", "d" }
# set_b = { "a", "e", "i", "c" }

# print("UNION", set_a.union(set_b))
# print("DIFFERENCE", set_a.difference(set_b))
# print("INTERSECTION", set_a.intersection(set_b)) 

vowels = ["a", "o", "u", "e", "i"]
word = input("Type word for search\n")

found_letters = set(vowels).intersection(set(word))

print("Found next vowel letters")
for letter in found_letters: 
  print(letter)
 