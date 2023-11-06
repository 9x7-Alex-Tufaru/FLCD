from HashTable import HashTable


class SymbolTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.hashTable = HashTable(capacity)

    def add(self, value):
        """
        Function to insert a value in the hash list
        :param value: the value to be added
        """
        self.hashTable.insert(value)
        return self.findPos(value)

    def getHashTable(self):
        return self.hashTable

    def remove(self, value):
        """
        Function to remove an item from the list
        :param value: the item to be removed
        """
        self.hashTable.remove(value)

    def __contains__(self, item):
        """
        Function to check if an item is in the hash list
        :param item: the item that the presence of is checked
        :return: True if the item is in the list, False otherwise
        """
        return self.hashTable.__contains__(item)

    def __str__(self):
        elements = self.hashTable.getAllElements()
        symbolTableString = "Position -> Symbol\n"
        for elem in elements:
            symbolTableString += str(elem[0]) + " -> " + str(elem[1]) + "\n"
        symbolTableString += "\n"
        return symbolTableString

    def findPos(self, item):
        """
        Function to get the position of an item in the list
        :param item: the item whose position is searched
        :return: the hash of the item if the item is in the list, -1 otherwise
        """
        return self.hashTable.findPos(item)
