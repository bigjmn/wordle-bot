def minifilter(i, letter, val):
    if val == 0:
        return lambda word: (letter in word) == False
    if val == 1:
        return lambda word: ((letter in word) and (word[i] != letter))
    if val == 2:
        return lambda word: word[i] == letter


def guessFilter(guess, result):
    def newFilter(word):
        for i in range(5):
            slotFilter = minifilter(i, guess[i], result[i])
            if slotFilter(word) == False:
                return False
        return True

    return newFilter
