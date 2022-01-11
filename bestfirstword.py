from scoreguess import scoreGuess
from makefilters import guessFilter
from config.listconfig import makeWordleMaster
import random

#find the expected value of every first word. Won't make it the 'best' overall, but
#might as well start somewhere
def getRemainders(guess, answer, fullList):
    result = scoreGuess(guess, answer)
    newFilter = guessFilter(guess, result)
    remainders = list(filter(newFilter, fullList))
    return len(remainders)

#actual brute forcing was too slow, so doing a random sample of answers for every guess
def bruteForce():
    allWords = makeWordleMaster()
    valueArray = []
    for i in range(len(allWords)):
        if i%20 == 0:


            print('word '+str(i)+' of '+str(len(allWords)))
        totalRemainders = 0
        firstWord = allWords[i]
        for j in range(2):
            answer = random.choice(allWords)
            pairResult = getRemainders(firstWord, answer, allWords)
            totalRemainders += pairResult
        totalRemainders /= len(allWords)

        valueArray.append(totalRemainders)
    return valueArray
k = bruteForce()
print(k.index(min(k)))
