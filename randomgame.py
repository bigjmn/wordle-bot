import random
from scoreguess import scoreGuess
from makefilters import guessFilter
from config.listconfig import makeWordleMaster

#one random round. Guess from random available word, get result
def randomRound(remainders, answer):
    randomguess = random.choice(remainders)
    result = scoreGuess(randomguess, answer)
    newFilter = guessFilter(randomguess, result)
    newRemainders = list(filter(newFilter, remainders))
    return newRemainders, (randomguess, result)

#game loop. guess, repeat, etc
def randomGame():
    guessHistory = []
    allWords = makeWordleMaster()
    print(len(allWords))
    answer = random.choice(allWords)
    guesses = 1
    solved = False

    while solved == False and guesses < 50:
        allWords, newstat = randomRound(allWords, answer)
        guessHistory.append(newstat)
        guesses += 1
        print(newstat)
        print(len(allWords))
        if newstat[0] == answer:
            solved = True

    print(guesses)
    return guessHistory

randomGame()
