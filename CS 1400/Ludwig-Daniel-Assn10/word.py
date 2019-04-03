
word = input('Enter a word: ')

letters = []
for i in word:
    letters.append(i)

nonDuplicate = []
for l in letters:
    if l not in nonDuplicate:
        nonDuplicate.append(l)


print(letters)
print(nonDuplicate)
