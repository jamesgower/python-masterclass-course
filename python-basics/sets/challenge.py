vowels = frozenset("aeiou")
letters = set(list(input("Enter a phrase: ")))

print(letters)
print(vowels)
print(sorted(letters.difference(vowels)))