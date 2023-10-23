from HashTable import HashTable


class SymbolTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.hashTable = HashTable(capacity)

    def add(self, value):
        self.hashTable.insert(value)

    def getHashTable(self):
        return self.hashTable

    def remove(self, value):
        self.hashTable.remove(value)

    def __contains__(self, item):
        return self.hashTable.__contains__(item)

    def __str__(self):
        return self.hashTable.__str__()

    def findPos(self, item):
        return self.hashTable.findPos(item)
