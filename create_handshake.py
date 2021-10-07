from reallySecureRandom import randomIntNumber


def createHandShake():
    '''
    First value represents the step parameter
    Second represents the size parameter
    '''
    randomStep = randomIntNumber(1,9)
    randomSize = randomIntNumber(1,100)
    return (randomStep, randomSize)

if __name__ == '__main__':
    test = createHandShake()
    print(test)
