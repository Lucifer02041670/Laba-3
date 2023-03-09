with open('synonyms.txt', 'r') as f:
    read = f.read()

    ListKey = []
    ListValue = []

    for line in read.split('\n'):
        if not line.strip():
            continue
        k, v = [word.strip() for word in line.split('-')]

        ListKey.append(k)
        ListValue.append(v)

for i, word1 in enumerate(ListKey):
    ListKey[i] = word1.lower()
for i, word1 in enumerate(ListValue):
    ListValue[i] = ListValue[i].lower()

print(ListKey)
print(ListValue)

WordID = input().lower()
s = ''
for i, word1 in enumerate(ListKey):
    if WordID == word1:
        print(ListValue[i].capitalize())
    elif WordID == ListValue[i]:
        print(ListKey[i].capitalize())

s = input('Синоним вам подходит Y/N(Д/Н): \n')
with open('synonyms.txt', 'a') as f:
    if s == 'N' or s == 'Н':
        newSin = input("Введите новый синоним: \n")
        f.write(f'{WordID} - {newSin}' + '\n')
    else:
        exit()

