from reallySecureRandom import randomIntNumber
from shuffleDict import createNewDict, shuffleWithDict
from shuffle_size import textLenthShuffle


def criptoFuncFlow(text: str, handShake: tuple):
    newDict = createNewDict(text)
    shuffledText = shuffleWithDict(newDict, text)
    shuffledSize = textLenthShuffle(shuffledText, handShake[1])
    return shuffledText
