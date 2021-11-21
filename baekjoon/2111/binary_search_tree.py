# 우선 이진 트리를 작성하고, 이를 이용하여 후위 순회 결과를 출력하자
from collections import deque

class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
    def setLeft(self, left):
        self.left = left
        left.parent = self
    def setRight(self, right):
        self.right = right
        right.parent = self

class Tree():
    def __init__(self):
        self.root = None
        self.nodes = []
    def setRoot(self, node):
        self.root = node
    def addNode(self, now,node):
        # 전위 순회 결과를 바탕으로 노드 추가
        if now.data > node.data :
            if not now.left:
                now.setLeft(node)
            else:
                self.addNode(now.left, node)
        if now.data < node.data:
            if not now.right:
                now.setRight(node)
            else:
                self.addNode(now.right, node)
    def makeTree(self,node):   
        if not self.nodes:
            self.setRoot(node)
        else:
            self.addNode(self.root,node)
    def showTree(self):
        q = deque([self.root])
        while q:
            now = q.popleft()
            l,r= None, None
            if now.left != None:
                q.append(now.left)
                l = now.left.data
            if now.right != None:
                q.append(now.right)
                r = now.right.data
            print(now.data, l,r)
    def postOrder(self,now):
        if now.left != None:
            self.postOrder(now.left)
        if now.right != None:
            self.postOrder(now.right)
        print(now.data)



nodeList = []
tree = Tree()
k = 0
while True:
    try:
        n = int(input())
        nodeList.append(Node(n))
        if k == 0:
            tree.setRoot(nodeList[0])
        else:
            # tree.addNode(nodeList[k-1], nodeList[k])
            tree.addNode(nodeList[0],nodeList[k])
        k += 1
    except:
        break
tree.postOrder(tree.root)
# while True:
#     try:
#         n = int(input())
#     except:
#         break