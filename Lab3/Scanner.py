import re

from PIF import PIF
from SymbolTable import SymbolTable


class Scanner:
    def __init__(self, capacity, operators, separators, reservedWords, fileName):
        self.PIF = PIF()
        self.symbolTable = SymbolTable(capacity)
        self.operators = operators
        self.separators = separators
        self.reservedWords = reservedWords
        self.fileName = fileName

    def getSymbolTable(self):
        return self.symbolTable

    def getPIF(self):
        return self.PIF

    def getTokens(self):
        """
        Gets the tokens from the source code
        """
        source = open(self.fileName, 'r')
        tokens = []
        lines = [line.strip() for line in source.readlines()]
        delimiters = self.separators + self.operators
        for line in lines:
            lineTokens = []
            currentToken = ""
            while line:
                foundDelimiter = False
                for delimiter in delimiters:
                    if line.startswith(delimiter):
                        if currentToken != "":
                            lineTokens.append(currentToken)
                            currentToken = ""
                        lineTokens.append(delimiter)
                        line = line[len(delimiter):]
                        foundDelimiter = True
                        break
                if not foundDelimiter:
                    currentToken += line[0]
                    line = line[1:]
            if currentToken != "":
                lineTokens.append(currentToken)
            tokens.append(lineTokens)
        source.close()
        return tokens

    def scan(self):
        """
        Classifies each token and places it in the ST and/or the PIF
        """
        tokens = self.getTokens()
        isLexicallyCorrect = True
        for i in range(len(tokens)):
            for token in tokens[i]:
                if self.isReservedWord(token) or self.isOperator(token) or self.isSeparator(token):
                    self.PIF.addToPIF(token, -1)
                elif self.isIdentifier(token) or self.isIntConstant(token) or self.isCharConstant(
                        token) or self.isStringConstant(token):
                    index = self.symbolTable.findPos(token)
                    if index == -1:
                        index = self.symbolTable.add(token)
                    if self.isIdentifier(token):
                        self.PIF.addToPIF("id", index)
                    else:
                        self.PIF.addToPIF("const", index)
                else:
                    print("Lexical error on line: " + str(i + 1) + ", token: " + token)
                    isLexicallyCorrect = False
        if isLexicallyCorrect:
            print("Lexically correct")

    def isSeparator(self, token):
        return token in self.separators

    def isOperator(self, token):
        return token in self.operators

    def isReservedWord(self, token):
        return token in self.reservedWords

    def isIdentifier(self, token):
        return re.search(r"^[A-Za-z]+[0-9]*$", token) is not None

    def isIntConstant(self, token):
        return re.search(r"0$|^([+]|-)?[1-9][0-9]*$", token) is not None

    def isCharConstant(self, token):
        return re.search(r"^'.'$", token) is not None

    def isStringConstant(self, token):
        return re.search(r'^".*?"$', token) is not None
