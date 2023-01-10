

def search_for_letters(phrase: str, letters: str = "aeuio") -> set:
  """Search any vowels found in an asked-for word."""
  found_letters = set(letters).intersection(set(phrase))
  
  return found_letters

def app(): 
  word = input('Type word for search\n')
  found_letters = search_for_letters(word)
  
  print('Found next vowel letters')
  for letter in found_letters: 
    print(letter)

if __name__ == '__main__':
  app()