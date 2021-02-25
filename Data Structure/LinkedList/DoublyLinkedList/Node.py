class Node:

    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.prev = self 
        self.next = self
    