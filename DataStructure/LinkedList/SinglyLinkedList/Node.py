class Node:

    def __init__(self, key = None, value = None):
        self.key = key         # 노드에 저장되는 key값으로 이 값으로 노드를 구분함
        self.value = value     # 추가 되는 정보가 있다면 value에 저장함
        self.next = None       # 다음에 연결될 노드의 주소

    def __str__(self):         # print함수를 이용해 출력할 때의 출력 문자열 리턴
        return str(self.key)