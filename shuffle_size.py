

def textLenthShuffle(text: str, shuffle_size: int):
    newText = text * int(shuffle_size)
    return newText


if __name__ == '__main__':
    EXAMPLE_TEXT = 'Ford Motor Company'
    newText = textLenthShuffle(EXAMPLE_TEXT, 2)
    print(newText)
