#Get the result array based on guess and answer
def scoreGuess(guess, answer):
    result = []
    for i in range(5):
        if guess[i] == answer[i]:
            result.append(2)
            continue
        if guess[i] in answer:
            result.append(1)
            continue
        result.append(0)
    return result
