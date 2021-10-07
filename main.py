from create_handshake import createHandShake
from cripto import criptoFuncFlow

EXAMPLE_TEXT = 'Ford Motor Company'

def main():
    handShake = createHandShake()
    shuffledFinalText = criptoFuncFlow(EXAMPLE_TEXT, handShake)
    print(shuffledFinalText)

if __name__ == '__main__':
    main()