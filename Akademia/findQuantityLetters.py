def find(str):
    letters = {}
    x = str.upper()
    test = str.upper().split(' ')
    print(test)
    for i in x:
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1
    return letters

print(find('mama to jest fajna Babka i lubi kiełabsę'))