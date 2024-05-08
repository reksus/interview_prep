"""
applications:
- finding dist b/w 2 nodes
- inheritance hierarchy in OOP
- as a subroutine in several adv. algo

algorithms:
- tarjan's offline lca
- heavy-light decomposition
- binary lifting
- etc.

covered in this impl:
Eulerian tour + Range Min Query (RMQ)

This can ans LCA in O(1)
with O(nlogn) preprocessing using a sparse table to do the RMQs

preprocessing can be improved to O(n) 
using Farach-Colton and Bender optimization

Algorithm:
1. make a tree rooted
2. all nodes are uniquely indexed [0...n-1]

  0
 1 2
    3

3. start a eulerian tour starting and ending at the root node
[0,1,0,2,3,2,0]

4. keep track of 
depth[] = [0,"1,(0),1,2",1,0] depth of each node by id
nodes[] = [0,"1,(0),2,3",2,0] pointer to each node in the order of visit
len of each list is 2n-1

each list is the lenght of the euler tour and index are the order in which the nodes are visited

5. find LCA(1, 3)
find the corresponding euler tour index?
1 : 1
3 : 4
what do if there are multiple indexes of visits?

keep another list
last[], index when the node was spotted last
this has length n only

"""

from typing import List
import math

class TreeNode:
    def __init__(self, id, parent=None) -> None:
        self.n = 1
        self.id = id
        self.parent = parent
        self.children = []
    
    def addChild(self, child):
        self.children.append(child)

def buildTree(graph, node):
    subtreeNodeCount = 1
    for nbr in graph[node.id]:
        if node.parent and node.parent.id == nbr:
            continue
        child = TreeNode(nbr, node)
        node.addChild(child)
        buildTree(graph, child)
        subtreeNodeCount += child.n
    node.n = subtreeNodeCount
    return node

def rootTree(graph, rootId):
    root = TreeNode(rootId)
    rootedTree = buildTree(graph, root)
    return rootedTree

def addUndirectedEdge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)

def createTree():
    n = 17

    tree = [[] for _ in range(n)]
    
    addUndirectedEdge(tree, 0, 1)
    addUndirectedEdge(tree, 0, 2)
    addUndirectedEdge(tree, 1, 3)
    addUndirectedEdge(tree, 1, 4)
    addUndirectedEdge(tree, 2, 5)
    addUndirectedEdge(tree, 2, 6)
    addUndirectedEdge(tree, 2, 7)
    addUndirectedEdge(tree, 3, 8)
    addUndirectedEdge(tree, 3, 9)
    addUndirectedEdge(tree, 5, 10)
    addUndirectedEdge(tree, 5, 11)
    addUndirectedEdge(tree, 7, 12)
    addUndirectedEdge(tree, 7, 13)
    addUndirectedEdge(tree, 11, 14)
    addUndirectedEdge(tree, 11, 15)
    addUndirectedEdge(tree, 11, 16)

    return rootTree(tree, 0)


class MinSparseTable:
    def __init__(self, values: List[int]) -> None:
        self.n = len(values)
        self.P = math.floor(math.log2(self.n))
        self.dp = [[0 for _ in range(self.n)] for _ in range(self.P + 1)]
        self.it = [[0 for _ in range(self.n)] for _ in range(self.P + 1)]
        self.log2 = [0 for _ in range(self.n+1)]
        
        for i, val in enumerate(values):
            self.dp[0][i] = val
            self.it[0][i] = i
            if i >= 2:
                self.log2[i] = self.log2[i // 2] + 1
        
        for p in range(1, self.P + 1):
            
            i = 0
            while i + (1 << p) <= self.n:
                
                # update range min
                leftRangeVal = self.dp[p-1][i]
                rightRangeVal = self.dp[p-1][i + (1 << (p - 1))]
                self.dp[p][i] = min(leftRangeVal, rightRangeVal)

                # update index
                if leftRangeVal <= rightRangeVal:
                    self.it[p][i] = self.it[p-1][i]
                else:
                    self.it[p][i] = self.it[p-1][i + (1 << (p - 1))]
                
                i += 1
    
    def minQuery(self, l, r):
        p = self.log2[r-l+1]
        k = 1 << p
        return min(self.dp[p][l], self.dp[p][r - k + 1])

    def minQueryIndex(self, l, r):
        p = self.log2[r - l + 1]
        k = 1 << p
        leftMinValue = self.dp[p][l]
        rightMinValue = self.dp[p][r - k + 1]
        if leftMinValue <= rightMinValue:
            return self.it[p][l]
        else:
            return self.it[p][r - k + 1]

class LCAEulerTour:
    def __init__(self, root) -> None:
        self.n = root.n
        self.tourIndex = 0
        self.setup(root)
    
    def setup(self, root):
        self.last = [-1 for _ in range(self.n)]
        tourSize = 2 * self.n - 1
        self.nodeDepth = [-1 for _ in range(tourSize)]
        self.nodeOrder = [-1 for _ in range(tourSize)]

        self.dfs(root, 0)

        # print(self.nodeDepth)
        # print(self.nodeOrder)
        # print(self.last)
        self.sparseTable = MinSparseTable(self.nodeDepth)
    
    def dfs(self, node, depth):
        if not root:
            return
        self.visit(node, depth)
        for child in node.children:
            self.dfs(child, depth+1)
            self.visit(node, depth)
    
    def visit(self, node, depth):
        self.last[node.id] = self.tourIndex
        self.nodeDepth[self.tourIndex] = depth
        self.nodeOrder[self.tourIndex] = node.id
        self.tourIndex += 1

    def lca(self, index1, index2):
        l = min(self.last[index1], self.last[index2])
        r = max(self.last[index1], self.last[index2])
        i = self.sparseTable.minQueryIndex(l, r)
        return self.nodeOrder[i]



if __name__ == "__main__":
    root = createTree()
    # print(root.children[1].children[0].children[1].id)
    # # idx  = [0,1, 2,3,4, 5,6]
    # values = [1,2,-3,2,4,-1,5]
    # sparseTable = MinSparseTable(values)
    # print(sparseTable.minQuery(1, 5))
    # print(sparseTable.minQueryIndex(1, 5))


    solver = LCAEulerTour(root)
    print(solver.lca(13, 14))
    print(solver.lca(9, 11))
    print(solver.lca(12, 12))


