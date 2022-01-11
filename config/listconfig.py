#   filter out non wordle words
def fiveDistinct(word):
    # word must be 5 letters long
    if len(word) != 5:
        return False
    #no repeat letters
    if len(set(word)) != 5:
        return False
    return True

# apply filter to dictionary 
def makeWordleMaster():
    with open('config/raw_common.txt', 'r') as common:
        commonList = common.read().splitlines()
        filtered = filter(fiveDistinct, commonList)
        return list(filtered)
