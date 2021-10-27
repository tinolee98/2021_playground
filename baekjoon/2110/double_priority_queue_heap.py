import heapq
import sys
N = int(input())
input = sys.stdin.readline

for _ in range(N):
    M = int(input().rstrip())
    minHeap, maxHeap = [],[]
    visited = [False for _ in range(int(1e6+1))]

    def Cleaning(heap):
        while heap and not visited[heap[0][1]]:
            heapq.heappop(heap)
    
    for key in range(M):
        c,n = list(input().rstrip().split())
        n = int(n)
        if c == "I":
            #print("insert")
            heapq.heappush(minHeap, (n,key))
            heapq.heappush(maxHeap, (n*-1,key))
            visited[key] = True
        else:
            #print("delete")
            if n == -1:
                Cleaning(minHeap)
                if minHeap:
                    visited[minHeap[0][1]] = False
                    heapq.heappop(minHeap)
            else:
                Cleaning(maxHeap)
                if maxHeap:
                    visited[maxHeap[0][1]] = False
                    heapq.heappop(maxHeap)
        #print("min",minHeap)
        #print("max", maxHeap)
    Cleaning(minHeap)
    Cleaning(maxHeap)
    if minHeap and maxHeap:
        print(-maxHeap[0][0], minHeap[0][0])
    else:
        print("EMPTY")