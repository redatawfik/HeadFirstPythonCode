phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

plist.pop(0)
plist.remove("'")
plist.insert(2,plist.pop(3))
plist.insert(4,plist.pop(5))
for n in range(4):
    plist.pop()

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
