word  = "bottles"
for bottles_number in range(5, 0 , -1):
  print(bottles_number, word, "of beer on the wall")
  print(bottles_number, word, "of beer")
  print("Take one down")
  print("Pass it around")

  if bottles_number == 1: 
    print("No more bottles of beer on the wall")
  else:
    new_num = bottles_number - 1
    if new_num == 1:
      word = "bottle"
    print(new_num, word, "of beer on the wall")
  print()