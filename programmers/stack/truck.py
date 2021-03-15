# 다리를 지나는 트럭 문제. 다리의 길이, 다리가 버틸 수 있는 하중, 트럭들의 무게를 알려주는 트럭 리스트를 받아 모든 트럭이 다리를 통과하는데 걸리는 시간을 출력하라.
from collections import deque
def solution(bridge_length, weight, truck_weights):
    queue = deque()
    sec = 1
    truck = truck_weights[::-1]
    for i in range(bridge_length-1):
        queue.append(0)
    queue.append(truck.pop())
    #print(queue, truck)
    while sum(queue) != 0:
        temp = 0
        first = queue[0]
        if len(truck) != 0:
            temp = truck.pop()
        if sum(queue)-first + temp > weight:
            truck.append(temp)
            temp = 0
        queue.append(temp)
        if len(queue) > bridge_length:
            queue.popleft()
        sec += 1
        #print(queue, truck)
    return sec

lst = list(map(int,input(">> ").split()))
lst2 = list(map(int,input(">> ").split()))
print(solution(lst[0],lst[1],lst2))