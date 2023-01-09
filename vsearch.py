

def search_for_vowels(word : str) -> set:
  """Search any vowels found in an asked-for word."""
  vowels = ['a', 'o', 'u', 'e', 'i']

  found_letters = set(vowels).intersection(set(word))
  
  return found_letters

def app(): 
  word = input('Type word for search\n')
  found_letters = search_for_vowels(word)
  
  print('Found next vowel letters')
  for letter in found_letters: 
    print(letter)

if __name__ == '__main__':
  app()