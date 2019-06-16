import random as rnd

listOfWords = ['tata', 'mama', 'kotek','morszczuk']

word = rnd.sample(listOfWords, 1)
wordToFind = list('_' * len(word[0]))
print(' '.join(wordToFind))
count = len(word[0])
score = 0
while count > 0:
    print('Give a letter')
    score += 1
    letter = input().upper()
    for x in range(len(word[0])):
        if (word[0][x].upper() == letter):
            wordToFind[x] = letter
            score -= 1
            count -=1
        if (score == 5):
            count = 0
    print(' '.join(wordToFind))
    # if (score - len(word[0]) < 0):
    #     score = 0
    # else:
    #     score = score - len(word[0])
        



print('\n', word[0].upper(), 'Your score is: ', score - len(word[0]))