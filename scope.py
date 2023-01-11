a = ["1"]

def some_func (b: list):
  original_b = b
  b = b + b
  print("is b equal new b?", b == original_b)


some_func(a)

print(a)