vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u':0}
found={}
word = input("Provide a word to search for vowels: ")
for letter in word:
    if letter in vowels:
        found.setdefault(letter,1)
        found[letter] += 1
for k, v in found.items():
    if (k):
        print(k, 'was found',v, 'times.')
