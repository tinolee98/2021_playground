import sys
N = int(input())
inputs = []
heap = []
input = sys.stdin.readline
for _ in range(N):
    inputs.append(int(input().rstrip()))
#print(inputs)

def insert(n,heap):
    heap.append(n)
    child = len(heap)-1
    parent = (child-1)//2
    if parent == -1:
        return
    childBig = True
    while  childBig and child > 0:
        parent = (child-1)//2
        if heap[parent] >= heap[child]:
            heap[parent],heap[child] = heap[child],heap[parent]
            child = parent
        else:
            childBig = False
        if child%2 == 1:
            pass
        else:
            pass
INF = 2**31+1
def delete():
    if len(heap) == 0:
        return 0
    heap[0],heap[-1] = heap[-1],heap[0]
    minimum = heap.pop()
    parent = 0
    while parent < len(heap):
        left,right = parent*2+1, parent*2+2
        leftValue = heap[left] if left < len(heap) else INF
        rightValue = heap[right] if right < len(heap) else INF
        if leftValue == INF and rightValue == INF:
            break
        elif leftValue < rightValue:
            if heap[parent] > leftValue:
                heap[parent],heap[left] = heap[left], heap[parent]
                parent = left
            else:
                break
        else:
            if heap[parent] > rightValue:
                heap[parent],heap[right] = heap[right], heap[parent]
                parent = right
            else:
                break
    return minimum

for n in inputs:
    if n == 0:
        print(delete())
    else:
        insert(n,heap)
