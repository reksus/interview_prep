import random
# tree invariant: 
# rules on imposed on tree after every operation to ensure that the invariant is alwasy satified
# Balance Factor: H (node.right) - H (node.left)

# and H is number of edges b/w the node and the farthest leaf

# RULE IS : BF should be either -1, 0, 1

class BBSTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.bf = 0  # <--- new data
        self.height = 0  # <--- new data


class BBSTree:

    def __init__(self):
        self.root = None
        self.nodeCount = 0

    def height(self):
        if not self.root: return 0
        return self.root.height

    def size(self):
        return self.nodeCount
    
    def isEmpty(self):
        return self.size() == 0

    def _contains(self, node, val):
        if not node:
            return False
        if node.val > val:
            return self._contains(node.left, val)
        elif node.val < val:
            return self._contains(node.right, val)
        return True
    
    def contains(self, val):
        print(f"check if {val} is present in the tree rooted at {'null' if not self.root else self.root.val}")
        return self._contains(self.root, val)

    def _remove(self, node, val):
        if not node: return None
        if node.val < val:
            return self._remove(node.right, val)
        elif node.val > val:
            return self._remove(node.left, val)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                newVal = self._findMax(node.left)
                node.val = newVal
                node.left = self._remove(node.left, newVal)

        self._update(node)
        return _balance(node)

    def _findMax(self, node):
        while node.right:
            node = node.right
        return node

    def _rightRotate(self, node):
        newParent = node.left
        node.left = newParent.right
        newParent.right = node
        # the order of update should be same as below and not vice versa
        self._update(node)
        self._update(newParent)
        return newParent

    def _leftRotate(self, node):
        newParent = node.right
        node.right = newParent.left
        newParent.left = node
        self._update(node)
        self._update(newParent)
        return newParent

    def _leftLeftCase(self, node):
        return self._rightRotate(node)
    
    def _rightRightCase(self, node):
        return self._leftRotate(node)
    
    def _leftRightCase(self, node):
        node.left = self._leftRotate(node.left)
        return self._leftLeftCase(node)

    def _rightLeftCase(self, node):
        node.right = self._rightRotate(node.right)
        return self._rightRightCase(node)

    def _balance(self, node):
        if node.bf == -2:
            if node.left.bf <= 0:
                return self._leftLeftCase(node)
            else:
                return self._leftRightCase(node)

        elif node.bf == +2:
            if node.right.bf >= 0:
                return self._rightRightCase(node)
            else:
                return self._rightLeftCase(node)
        else:
            return node

    def _update(self, node):
        lh = node.left.height if node.left else -1
        rh = node.right.height if node.right else -1

        node.height = 1 + max(lh, rh)
        node.bf = rh - lh

    def _insert(self, node, val):
        if not node:
            return BBSTreeNode(val)
        if node.val < val:
            node.right = self._insert(node.right, val)
        else:
            node.left = self._insert(node.left, val)

        self._update(node)
        return self._balance(node)

    def insert(self, val):
        if not val: return False
        if not self._contains(self.root, val):
            self.root = self._insert(self.root, val)
            self.nodeCount += 1
            print(f"nodeCount {self.nodeCount}")
            return True
        return False

    def remove(self, val):
        if not val or not self._contains(self.root, val):  return False
        self.root = self._remove(self.root, val)
        self.nodeCount -= 1
        return True

    def _printtree(self, root):
        if not root: return
        self._printtree(root.left)
        print(root.val, root.height, root.bf)
        self._printtree(root.right)

    def printtree(self):
        self._printtree(self.root)
    

if __name__ == "__main__":
    bbst = BBSTree()
    for _ in range(1, 6):
        # r = random.randint(-99, 99)
        r = _
        print(r)
        bbst.insert(r)
    bbst.printtree()