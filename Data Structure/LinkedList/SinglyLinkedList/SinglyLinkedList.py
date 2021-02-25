from Node import *
	
class SinglyLinkedList:
	def __init__(self):
		self.head = None
		self.size = 0
	
	def __len__(self):
		return self.size
	
	def printList(self): # 변경없이 사용할 것!
		v = self.head
		while(v):
			print(v.key, "->", end=" ")
			v = v.next
		print("None")
	
	def pushFront(self, key):
		new_node = Node(key)
		new_node.next = self.head
		self.head = new_node
		self.size += 1

	def pushBack(self, key):
		new_node = Node(key)
		if len(self) > 0:
			current = self.head
			while current.next != None:
				current = current.next
			current.next = new_node
		else:
			self.head = new_node
		self.size += 1
		
	def popFront(self): 
		# head 노드의 값 리턴. empty list이면 None 리턴
		if len(self) > 0:
			key = self.head.key
			head = self.head
			self.head = self.head.next
			self.size -= 1
			del head
			return key
		else:
			return None
			
	def popBack(self):
		# tail 노드의 값 리턴. empty list이면 None 리턴
		if len(self) > 1:
			prev, tail = None, self.head
			while tail.next != None:
				prev = tail
				tail = tail.next
			prev.next = tail.next
			key = tail.key
			self.size -= 1
			del tail
			return key
		elif len(self) == 1:
			head = self.head
			key = head.key
			self.size -= 1
			del head
			return key
		else:
			return None

	def search(self, key):
		# key 값을 저장된 노드 리턴. 없으면 None 리턴
		v = self.head
		while v:
			if v.key == key:
				return v
			v = v.next
		return None
		
	def remove(self, x):
		# 노드 x를 제거한 후 True리턴. 제거 실패면 False 리턴
		if x.key == self.head:
			head = self.head
			self.head = self.head.next
			self.size -= 1
			del head
			return True
		else:
			prev, current = None, self.head
			while current: # 첫번째 노드가 아닌 경우
				if current.key == x.key:
					prev.next = current.next
					self.size -= 1
					del current
					return True
				prev = current
				current = current.next
			return False
		 
	

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