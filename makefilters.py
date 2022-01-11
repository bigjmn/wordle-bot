# create filter based on result of particular letter placement
# 0 if not in word, 1 if in wrong place, 2 if in right place
def minifilter(i, letter, val):
    if val == 0:
        return lambda word: (letter in word) == False
    if val == 1:
        return lambda word: ((letter in word) and (word[i] != letter))
    if val == 2:
        return lambda word: word[i] == letter

# compiles mini filters
# returns a filter based on the word and result (array of 5 0/1/2 values)
def guessFilter(guess, result):
    def newFilter(word):
        for i in range(5):
            slotFilter = minifilter(i, guess[i], result[i])
            if slotFilter(word) == False:
                return False
        return True

    return newFilter
