import random

class BSTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BSTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, root, node):
        if not self.root:
            self.root = node
        else:
            if root.val < node.val:
                if not root.right:
                    root.right = node
                else:
                    self.insert(root.right, node)
            else:
                if not root.left:
                    root.left = node
                else:
                    self.insert(root.left, node)

    def inorder(self, root):
        if not root:
            return

        self.inorder(root.left)
        print(root.val, end=" ")
        self.inorder(root.right)

    def inorder_successor(self, node):
        if not node.right:
            return None
        curr = node.right
        while (curr.left):
            curr = curr.left
        return curr

    def inorder_predecessor(self, node):
        if not node.left:
            return None
        curr = node.left
        while (curr.right):
            curr = curr.right
        return curr

    def delete(self, root, val):
        if not root:
            return None

        if root.val < val:
            root.right = self.delete(root.right, val)
        elif root.val > val:
            root.left = self.delete(root.left, val)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            node = self.inorder_predecessor(root)
            root.val = node.val
            root.left = self.delete(root.left, root.val)
        
        return root
            
    def check_correctness_using_range(self, root):
        # idea: pass the [min, max] var to each node the root should lie b/t this range
        pass
    
    def check_correctness_using_inorder(self, root):
        # inorder traversal yiels a sorted list
        # so keep the prev value and always compare with the currently processing node
        pass 

    
if __name__ == "__main__":    
    bst = BSTree()

    for _ in range(5):
        r = random.randint(-100, 100)
        print(r)
        bst.insert(bst.root, BSTreeNode(r))

    print("root ", bst.root.val)
    bst.inorder(bst.root)
    print()
    # suc = bst.inorder_successor(bst.root)
    # if suc:
    #     print(suc.val)
    # pre = bst.inorder_predecessor(bst.root)
    # if pre:
    #     print(pre.val)

    del_val = bst.root.val
    print(del_val)
    root = bst.delete(bst.root, del_val)
    bst.inorder(root)
    print()
    
        