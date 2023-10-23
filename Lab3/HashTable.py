class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def _hash(self, item):
        """
        Function to find the hash of an item
        :param item: the item we want to find the hash of
        :return: the hash value mod the capacity of the table
        """
        return hash(item) % self.capacity

    def insert(self, value):
        """
        Function to insert a value in the hash table
        :param value: the value to be added
        """
        if self.__contains__(value):
            return
        index = self._hash(value)
        if self.table[index] is None:
            self.table[index] = Node(value)
            self.size += 1
        else:
            current = self.table[index]
            new_node = Node(value)
            new_node.next = self.table[index]
            self.table[index] = new_node
            self.size += 1

    def remove(self, value):
        """
        Function to remove an item from the table
        :param value: the item to be removed
        """
        index = self._hash(value)
        previous = None
        current = self.table[index]

        while current:
            if current.value == value:
                if previous:
                    previous.next = current.next
                else:
                    self.table[index] = current.next
                self.size -= 1
                return
            previous = current
            current = current.next

    def __contains__(self, item):
        """
        Function to check if an item is in the hash table
        :param item: the item that the presence of is checked
        :return: True if the item is in the table, False otherwise
        """
        for i in range(len(self.table)):
            current = self.table[i]
            while current:
                if current.value == item:
                    return True
                else:
                    current = current.next
        return False

    def __str__(self):
        elements = []
        for i in range(self.capacity):
            current = self.table[i]
            while current:
                elements.append((i, current.value))
                current = current.next
        return str(elements)

    def findPos(self, item):
        """
        Function to get the position of an item in the table
        :param item: the item whose position is searched
        :return: the hash of the item if the item is in the table, -1 otherwise
        """
        if not self.__contains__(item):
            return -1
        return self._hash(item)
