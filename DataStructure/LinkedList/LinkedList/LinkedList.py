class Node:
    
    def __init__(self,data):
        self.data = data #  노드가 저장하는 데터
        self.next = None


# node 객체 생성
head_node = Node(2)
node_1 = Node(3)
node_2 = Node(5)
node_3 = Node(7)
tail_node = Node(11)

# 노드들을 연결
head_node.next = node_1
node_1.next = node_2
node_2.next = node_3
node_3.next = tail_node

# 노드 순서대로 출력
iterator = head_node

while iterator is not None:
    print(iterator.data)
    iterator = iterator.next

class LinkedList:
    """링크드 리스트 클래스"""

    def __init__(self):
        self.head = None
        self.tail = None

    def find_node_at(self, index):
        """링크드 리스트 접근 연산 메소드. 파라미터 인덱스는 항상 있다고 가정"""
        iterator = self.head

        for _ in range(index):
            iterator = iterator.next

        return iterator
    
    def find_node_with_data(self, data):
        """링크드 리스트에서 탐색 연산 메소드. 단, 해당 노드가 없으면 None을 리턴한다"""
        iterator = self.head  # 링크드 리스트를 돌기 위해 필요한 노드 변수

        # 링크드 리스트 전체를 돈다
        while iterator is not None:
            # iterator 노드의 데이터가 찾는 데이터면 iterator를 리턴한다
            if iterator.data == data:
                return iterator
            iterator = iterator.next  # 다음 노드로 넘어간다

        # 링크드 리스트 안에 원하는 데이터가 없었기 때문에 None 리턴한다
        return None 

    def append(self, data):
        """링크드 리스트 추가 연산 메소드"""

        # 노드 생성
        new_node = Node(data)

        if self.head is None: # 링크드 리스트가 비어있는 경우
            self.head = new_node
            self.tail = new_node
        else: # 링크드 리스트가 비어 있지 않은 경우
            self.tail.next = new_node
            self.tail = new_node

    def __str__(self):
        """링크드 리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = "|"

        # 링크드  리스트 안에 모든 노드를 돌기 위한 변수. 일단 가장 앞 노드로 정의한다.
        iterator = self.head

        # 링크드  리스트 끝까지 돈다
        while iterator is not None:
            # 각 노드의 데이터를 리턴하는 문자열에 더해준다
            res_str += f" {iterator.data} |"
            iterator = iterator.next  # 다음 노드로 넘어간다

        return res_str

ll = LinkedList()
ll.append(1)
ll.append(3)
ll.append(4)

print(ll.find_node_at(1).data)
ll.find_node_at(1).data = 6
print(ll)