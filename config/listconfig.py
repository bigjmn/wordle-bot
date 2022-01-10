def fiveDistinct(word):
    if len(word) != 5:
        return False
    if len(set(word)) != 5:
        return False
    return True

def makeWordleMaster():
    with open('config/raw_common.txt', 'r') as common:
        commonList = common.read().splitlines()
        filtered = filter(fiveDistinct, commonList)
        return list(filtered)
