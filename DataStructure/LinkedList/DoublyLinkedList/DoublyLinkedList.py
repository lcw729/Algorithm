from Node import *

class DoublyLinkedList:

    def __init__(self):
        self.head = Node() # Dummy 노드로만 이루어진 빈 리스트
        self.size = 0

    def printList(self):
        current = self.head.next
        print("h ->", end=" ")
        while current != self.head:
            print(current.key, "->", end=" ")
            current = current.next
        print("h")
    
    def first(self):
        return self.head.next.key

    def last(self):
        return self.head.prev.key
        

    def splice(self, a, b, x): # cut [a, b] after x --> O(1)
        ap = a.prev
        bn = b.next
        ap.next = bn
        bn.prev = ap # 잘려 나간 부분을 연결

        xn = x.next # x의 다음 노드 
        xn.prev = b # x의 다음 노드의 prev 설정
        b.next = xn 
        x.next = a # x의 next 설정
        a.prev = x # a의 prev 설정

    def moveAfter(self, a, x): # O(1)
        self.splice(a, a, x)

    def moveBefore(self, a, x): # O(1)
        self.splice(a, a, x.prev)

    def insertAfter(self, a, key): # O(1)
        # new_node = Node(key)
        # a.next.prev = new_node
        # new_node.next = a.next
        # a.next = new_node
        # new_node.prev = a
        self.moveAfter(Node(key), a)
        
    def insertBefore(self, a, key): # O(1)
        # new_node = Node(key)
        # a.prev.next = new_node
        # new_node.prev = a.prev
        # a.prev = new_node
        # new_node.next = a
        self.moveBefore(Node(key), a)

    def pushFront(self, key): # O(1)
        self.insertAfter(self.head, key)
    
    def pushBack(self, key): # O(1)
        self.insertBefore(self.head, key)

    def deleteNode(self, x): # O(1)
        if x == None or x == self.head:
            return None
        else:
            key = x.key
            x.prev.next = x.next
            x.next.prev = x.prev
            del x
            return key

    def popFront(self): # O(1)
        key = self.head.next.key
        head = self.head
        secondNode = self.head.next.next
        head.next = secondNode
        secondNode.prev = head
        return key
    
    def popBack(self): # O(1)
        key = self.head.prev.key
        head = self.head
        backSecondeNode = self.head.prev.prev
        head.prev = backSecondeNode
        backSecondeNode.next = head
        return key 

    def search(self, key): # o(n)
        current = self.head.next
        while current != self.head:
            if current.key == key: 
                return current
            current = current.next
        return None

L = DoublyLinkedList()
while True:
    cmd = input().split()
    if cmd[0] == 'pushF':
        L.pushFront(int(cmd[1]))
        print("+ {0} is pushed at Front".format(cmd[1]))
    elif cmd[0] == 'pushB':
        L.pushBack(int(cmd[1]))
        print("+ {0} is pushed at Back".format(cmd[1]))
    elif cmd[0] == 'popF':
        key = L.popFront()
        if key == None:
            print("* list is empty")
        else:
            print("- {0} is popped from Front".format(key))
    elif cmd[0] == 'popB':
        key = L.popBack()
        if key == None:
            print("* list is empty")
        else:
            print("- {0} is popped from Back".format(key))
    elif cmd[0] == 'search':
        v = L.search(int(cmd[1]))
        if v == None: print("* {0} is not found!".format(cmd[1]))
        else: print(" * {0} is found!".format(cmd[1]))
    elif cmd[0] == 'insertA':
        # inserta key_x key : key의 새 노드를 key_x를 갖는 노드 뒤에 삽입
        x = L.search(int(cmd[1]))
        if x == None: print("* target node of key {0} doesn't exit".format(cmd[1]))
        else:
            L.insertAfter(x, int(cmd[2]))
            print("+ {0} is inserted After {1}".format(cmd[2], cmd[1]))
    elif cmd[0] == 'insertB':
        # inserta key_x key : key의 새 노드를 key_x를 갖는 노드 앞에 삽입
        x = L.search(int(cmd[1]))
        if x == None: print("* target node of key {0} doesn't exit".format(cmd[1]))
        else:
            L.insertBefore(x, int(cmd[2]))
            print("+ {0} is inserted Before {1}".format(cmd[2], cmd[1]))
    elif cmd[0] == 'delete':
        x = L.search(int(cmd[1]))
        if x == None:
            print("- {0} is not found, so nothing happens".format(cmd[1]))
        else:
            L.deleteNode(x)
            print("- {0} is deleted".format(cmd[1]))
    elif cmd[0] == "first":
        print("* {0} is the value at the front".format(L.first()))
    elif cmd[0] == "last":
        print("* {0} is the value at the back".format(L.last()))
    elif cmd[0] == 'print':
        L.printList()
    elif cmd[0] == 'exit':
        break
    else:
        print("* not allowed command. enter a proper command!")