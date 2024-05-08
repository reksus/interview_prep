class TreeNode:
    def __init__(self, id, parent=None, children=[]) -> None:
        self.id = id
        self.children = children if children else []

    def addChild(self, node):
        self.children.append(node)
        
def encode(node) -> str:
    if not node:
        return ""
    labels = []
    for child in node.children:
        labels.append(encode(child))
    labels.sort()
    return "(" + "".join(labels) + ")"

def buildTree(graph, node) -> TreeNode:
    from collections import deque
    q = deque()
    q.append(node)
    vis = set()
    vis.add(node.id)
    while q:
        curr = q.popleft()
        for nbr in graph[curr.id]:
            if nbr not in vis:
                child = TreeNode(nbr)
                curr.addChild(child)
                q.append(child)
                vis.add(nbr)
    
    return node

def rootTree(graph, rootId) -> TreeNode:
    root = TreeNode(rootId)
    return buildTree(graph, root)

def findTreeCenter(tree):
    n = len(tree)
    degree = [len(node) for node in tree]
    leaves = [i for i in range(len(tree)) if len(tree[i]) == 1]
    processedLeaves = len(leaves)
    while processedLeaves < n:
        newLeaves = []
        for leaf in leaves:
            
            for nbr in tree[leaf]:
                degree[nbr] -= 1
                if degree[nbr] == 1:
                    newLeaves.append(nbr)
            degree[leaf] = 0 
        processedLeaves += len(newLeaves)
        leaves = newLeaves
    
    return leaves

def areTreesIsomorphic(tree1, tree2):
    if not tree1 or not tree2:
        raise Exception("trees cant be empty")
    center1 = findTreeCenter(tree1)
    center2 = findTreeCenter(tree2)

    print("center1", center1)
    print("center2", center2)
    rootedTree1 = rootTree(tree1, center1[0])
    tree1Encoding = encode(rootedTree1)
    print(tree1Encoding)

    for center in center2[::-1]:
        rootedTree2 = rootTree(tree2, center)
        tree2Encoding = encode(rootedTree2)
        print(tree2Encoding)
        if tree1Encoding == tree2Encoding:
            return True
        
    return False

def addUndirectedEdge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)

def simpleIsomorphismTest():
    tree1 = [[] for _ in range(5)]
    addUndirectedEdge(tree1, 2, 0);
    addUndirectedEdge(tree1, 3, 4);
    addUndirectedEdge(tree1, 2, 1);
    addUndirectedEdge(tree1, 2, 3);
    
    tree2 = [[] for _ in range(5)]
    addUndirectedEdge(tree2, 1, 0);
    addUndirectedEdge(tree2, 2, 4);
    addUndirectedEdge(tree2, 1, 3);
    addUndirectedEdge(tree2, 1, 2);

    print(tree1)
    print(tree2)
    print(f"are trees isomorphic {areTreesIsomorphic(tree1, tree2)}")
    # if not areTreesIsomorphic(tree1, tree2):
    #     print("trees should be isomorphic")

if __name__ == "__main__":
    simpleIsomorphismTest()

