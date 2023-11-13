from Scanner import Scanner


def getTokensFromFile():
    file = open("Tokens.in", 'r')
    operators = []
    separators = []
    reservedWords = []
    lines = [line.strip() for line in file.readlines()]
    for line in lines:
        elements = line.split()
        if elements[1] == "operator":
            operators.append(elements[0])
        elif elements[1] == "separator":
            separators.append(elements[0])
        elif elements[1] == "reserved_word":
            reservedWords.append(elements[0])
    return operators, separators, reservedWords


def printResultToFile(scanner):
    scanner.scan()
    pif = open("PIF.out", 'a')
    pif.write(scanner.fileName + "\n")
    pif.write(str(scanner.PIF))
    pif.close()
    st = open("ST.out", 'a')
    st.write(scanner.fileName + "\n")
    st.write(str(scanner.symbolTable))
    st.close()


def runScanner():
    operators, separators, reservedWords = getTokensFromFile()
    separators.append(' ')
    open("PIF.out", 'w').close()
    open("ST.out", 'w').close()
    scanner1 = Scanner(7, operators, separators, reservedWords, "p1.txt")
    scanner2 = Scanner(7, operators, separators, reservedWords, "p2.txt")
    scanner3 = Scanner(7, operators, separators, reservedWords, "p3.txt")
    scanner1_err = Scanner(7, operators, separators, reservedWords, "p1_err.txt")
    printResultToFile(scanner1)
    # printResultToFile(scanner2)
    # printResultToFile(scanner3)
    # printResultToFile(scanner1_err)


if __name__ == '__main__':
    runScanner()
