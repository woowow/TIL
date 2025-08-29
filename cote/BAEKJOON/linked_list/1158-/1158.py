'''
N명이 앉아있고, K번째 사람이 계속해서 빠져나감
N명의 사람이 모두 제거될 때까지 완성
제거되는 순서를 출력
시간을 아끼기 위해, 제거되는 순서(pop을 list에 저장해서 마지막에 한 번에 출력)
1,2,3,4,5,6,7이고 앞에서부터 K번씩 사라짐

그냥 K가 N을 넘어가면 앞으로 돌리면 됨
단, 이미 사라진 사람을 고려해야함
K번째 index를 삭제하면 O(N), 해당 과정을 N번 반복해야하므로 O(N^2) = 5000*5000, 25,000,000
삭제해야할 것을 끝에 놓는 방법?

append, pop()을 사용해야 O(1)

'''

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

N, K = map(int, input().split())

left = [i for i in range(1, N+1)]

head = Node(1)
prev = head

for i in range(2, N+1):
    node = Node(i)
    prev.next = node
    node.prev = prev
    prev = node

prev.next = head
head.prev = prev

cur = head
result = []

rest = N

while rest > 0:
    for _ in range(K-1):
        cur = cur.next
    result.append(str(cur.val))

    cur.prev.next = cur.next
    cur.next.prev = cur.prev
    cur = cur.next
    rest -= 1

print("<"+", ".join(result)+">")