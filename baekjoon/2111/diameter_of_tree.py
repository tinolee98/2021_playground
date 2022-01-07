N = int(input())
class Node:
    def __init__(self,data,parent=None):
        self.data = data
        self.children = []
        self.parent = parent
        self.distList = []
        self.dist = {}
    def addDist(self, childData,l):
        if childData not in self.dist:
            self.dist[childData] = l
        else:
            self.dist[childData] += l
        self.distList.append(self.dist[childData])
nodes = [None]*(N+1)

for _ in range(N-1):
    parent, child, l = list(map(int, input().split()))
    if nodes[parent] == None:
        nodes[parent] = Node(parent)
    if nodes[child] == None:
        nodes[child] = Node(child,nodes[parent])
    now = nodes[parent]
    while now.parent:
        break
    nodes[parent].dist[child] = l
    print(nodes[parent].dist)
        
    


# # from collections import deque
# # N = int(input())
# # d = [[0 for _ in range(N+1)] for _ in range(N+1)]
# # ways = [[]for _ in range(N+1)]
# # graph = [[]for _ in range(N+1)]

# # for _ in range(N-1):
# #     a,b,l = list(map(int, input().split()))
# #     graph[a].append((b,l))
# #     graph[b].append((a,l))
# # print(graph)

# # leaves = []
# # for i in range(len(graph)):
# #     if len(graph[i]) == 1:
# #         leaves.append(i)
# # print(leaves)

# # def FindWay(start, end):
# #     print(start, end)

# # for i,start in enumerate(leaves):
# #     for end in leaves[i+1:]:
# #         print(start, end)

# # def D(points, d,now):
# #     visited = [False]*(N+1)
# #     q = deque(points)
# #     while q:
# #         pastNode,node = q.popleft()
# #         if not visited[node]:
# #             visited[node] = True
# #             q += graph[node]
# #             if now != node:
# #                 d[now][node] = d[now][pastNode] + d[pastNode][node]
# #                 d[node][now] = d[now][node]

# # for i in range(1,N):
# #     start, end, l = list(map(int, input().split()))
# #     d[start][end] = l
# #     d[end][start] = l
# #     graph[start].append((start,end))
# #     graph[end].append((end,start))
# # leaves = []
# # for i in range(len(graph)):
# #     if len(graph[i]) == 1:
# #         leaves.append(i)

# # maximum = 0
# # for i,start in enumerate(leaves):
# #     D([(start,start)],d,start)
# #     maximum = max(maximum, max(d[start]))
# # print(maximum)


# N = int(input())

# class Node:
#     def __init__(self,data):#,  child=None, l=0):
#         self.parent = None
#         self.data = data
#         self.children = []
#     def addChild(self, child,l):
#         self.children.append((child,l))
#     def addParent(self, parent,l):
#         self.parent = (parent,l)
#     def isLeaf(self):
#         if len(self.children) == 0:
#             return True
#         return False

# nodeList = [None]*(N+1)
# isExist = [False]*(N+1)
# leaves = []
# for _ in range(N-1):
#     parentData, childData, l = list(map(int,input().split()))
#     if not isExist[parentData]:
#         nodeList[parentData] = Node(parentData)
#         isExist[parentData] = True
#     if not isExist[childData]:
#         nodeList[childData] = Node(childData)
#         isExist[childData] = True
#     nodeList[parentData].addChild(nodeList[childData],l)
#     nodeList[childData].addParent(nodeList[parentData],l)

# print("leaves")
# for node in nodeList[1:]:
#     if node.isLeaf():
#         leaves.append(node)
#         print(node.data)

# # 항상 부모 -> 자녀 거리를 받을 수 있도록 통일 해줘야 편할듯
# # 리스트로 만들기 ㄱㄱ

# def DFS(start,now,visited):
#     visited[now.data] = True
#     maximum = 0
#     print("IN",now.data)
#     if start != now and now.isLeaf():
#         maximum = now.parent[1]
#     if now.parent != None and not visited[now.parent[0].data]:
#         # checkList.append(now.parent[0])
#         print("go parent")
#         maximum = DFS(start,now.parent[0],visited)+now.parent[1]
#     if not now.isLeaf():
#         for child in now.children:
#             if not visited[child[0].data]:
#                 # checkList.append(child)
#                 print("go child")
#                 if now.parent:
#                     maximum = max(DFS(start,child[0],visited)+now.parent[1],maximum)#+child[1], maximum)
#                     # 이부분이 문제임!
#                 else:
#                     maximum = max(DFS(start,child[0],visited),maximum)#+child[1], maximum)

#     print("result\t",start.data,now.data, maximum)
#     # for nextNode in checkList:
#     return maximum

# for leaf in leaves:
#     visited = [False]*(N+1)
#     print("DFS")
#     start = leaf
#     print(DFS(start,leaf, visited))
    