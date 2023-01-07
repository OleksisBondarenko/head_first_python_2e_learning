phrase = "Don't panic!"
plist = list(phrase)
new_phrase = []

new_phrase = "".join(plist[1:3])
new_phrase += "".join([plist.pop(5), plist.pop(4), "".join(plist[5: 3: -1])])

print(plist)
print(new_phrase)