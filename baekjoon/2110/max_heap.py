N = int(input())

INF = 2**31
nums = []
for _ in range(N):
    nums.append(int(input()))
heap = []


def delete(n,heap):
    if len(heap) == 0:
        return 0
    heap[0], heap[-1] = heap[-1],heap[0]
    result = heap.pop()
    parent = 0
    while parent < len(heap):
        left,right = parent*2+1, parent*2+2
        leftValue = heap[left] if left < len(heap) else 0
        rightValue = heap[right] if right < len(heap) else 0
        if leftValue == 0 and rightValue == 0:
            break
        elif leftValue > rightValue:
            if heap[parent] < leftValue:
                heap[parent],heap[left] = heap[left], heap[parent]
                parent = left
            else:
                break
        else:
            if heap[parent] < rightValue:
                heap[parent],heap[right] = heap[right], heap[parent]
                parent = right
            else:
                break
    return result



def insert(n,heap):
    child = len(heap)
    heap.append(n)
    while child > 0:
        parent = (child-1)//2
        if heap[child] > heap[parent]:
            heap[child], heap[parent] = heap[parent], heap[child]
            child = parent
        else:
            break

for n in nums:
    if n == 0:
        print(delete(n,heap))
    else:
        insert(n,heap)
    #print(heap)
