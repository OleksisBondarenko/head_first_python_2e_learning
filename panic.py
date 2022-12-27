phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

# remove, pop, append, extend, insert
# on tap
plist.pop(0)
plist.remove("'")
plist.insert(2, plist.pop(3))
plist.extend([plist.pop(4), plist.pop(3) ] )
plist.insert(4, plist.pop(-2))
plist.insert(3, plist.pop(-1))
for i in range(4):
  plist.pop(-1)

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)