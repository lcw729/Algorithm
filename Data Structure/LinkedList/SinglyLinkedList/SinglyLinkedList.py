from Node import *

class SinglyLinkedList:

    def __init__(self):
        self.head = None # head 노드를 저장함
        self.size = 0    # 리스트의 노드 개수를 저장함

    def printList(self): # 변경없이 사용할 것!
        v = self.head
        while(v):
            print(v.key, "->", end=" ")
            v = v.next
        print("None")

    def __len__(self):   # len(L) :  리스트 L의 size 리턴
        return self.size

    def pushFront(self, key):
        new_node = Node(key)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pushBack(self, key):
        new_node = Node(key)
        if self.size == 0:
            self.head = new_node
        else:  
            tail = self.head
            while tail.next != None:
                tail = tail.next
            tail.next = new_node
        self.size += 1

    def popFront(self):
        if self.size == 0:
            return None
        else:
            head = self.head
            key = head.key
            self.head = self.head.next
            self.size -= 1
            del head
            return key


    def popBack(self):
        if self.size <= 1:
            return self.popFront()
        else:
            prev, tail = None, self.head
            while tail.next != None:
                prev = tail
                tail = tail.next
            prev.next = tail.next
            key = tail.key
            self.size -= 1
            del tail
            return key

    def remove(self, v):
        prev, current = None, self.head
        if v.key == current.key:
            self.head = self.head.next
            self.size -= 1
            del current 
            return True
        while current:
            if current.key == v.key:
                prev.next = current.next
                self.size -= 1
                del current
                return True
            prev = current
            current = current.next
        return None

    def search(self, key):
        v = self.head
        while v:
            if v.key == key:
                return v
            v = v.next
        return None 

    
    # def size(self):
    #     return self.size

    def __iter__(self):
        v = self.head
        while v != None:
            yield v
            v = v.next

L = SinglyLinkedList()
while True:
    cmd = input().split()
    if cmd[0] == "pushFront":
        L.pushFront(int(cmd[1]))
        print(int(cmd[1]), "is pushed at front.")
    elif cmd[0] == "pushBack":  
        L.pushBack(int(cmd[1]))
        print(int(cmd[1]), "is pushed at back.")
    elif cmd[0] == "popFront":
        x = L.popFront()
        if x == None:
            print("List is empty.") 
        else:
            print(x, "is popped from front.")
    elif cmd[0] == "popBack":
        x = L.popBack()
        if x == None:
            print("List is empty.")
        else:
            print(x, "is popped from back.")    
    elif cmd[0] == "search":
        x = L.search(int(cmd[1]))
        if x == None:
            print(int(cmd[1]), "is not found!")
        else:
            print(int(cmd[1]), "is found!")
    elif cmd[0] == "remove":
        x = L.search(int(cmd[1]))
        if L.remove(x):     
            print(x.key, "is removed.")
        else:
            print("Key is not removed for some reason.")
    elif cmd[0] == "printList":
        L.printList()
    elif cmd[0] == "size":
        print("list has", len(L), "nodes.")
    elif cmd[0] == "exit":
        print("DONE!")
        break
    else:
        print("Not allowed operation! Enter a legal one!")
    