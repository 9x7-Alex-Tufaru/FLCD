class PIF:
    def __init__(self):
        self.list = []

    def addToPIF(self, name, pos):
        """
        Function to add a token to the PIF
        """
        self.list.append((name, pos))

    def __str__(self):
        pifStr = "Token -> ST_pos\n"
        for elem in self.list:
            pifStr += str(elem[0]) + " -> " + str(elem[1]) + "\n"
        pifStr += "\n"
        return pifStr
