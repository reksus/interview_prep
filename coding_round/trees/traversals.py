# tree node definition
class TreeNode:
    def __init__(self, data: int, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    
    def get_data(self):
        return self.data

    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right
    
    def set_left(self, left):
        if not isinstance(left, TreeNode):
            raise TypeError('left must be an instance of TreeNode')
        self.left = left
    
    def set_right(self, right):
        if not isinstance(right, TreeNode):
            raise TypeError('right must be an instance of TreeNode')
        self.right = right

    def __str__(self):
        return str(self.data)
    

def preorder_iterative(root):
    if not root:
        return
    result = []
    stack = []
    stack.append(root)
    while stack:
        curr = stack.pop()
        if curr.get_right(): stack.append(curr.get_right())
        if curr.get_left(): stack.append(curr.get_left())
        result.append(curr.data)  # process the element
    return result

    
def inorder_iterative(root):
    if not root:
        return
    result = []
    stack = []
    curr = root
    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            result.append(curr.data)  # process the element
            curr = curr.right
    return result


def postorder_iterative(root):
    if not root:
        return
    result = []
    stack = []
    curr = root
    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            temp = stack[-1].right
            if not temp:
                temp = stack.pop()
                result.append(temp.data)  # process the element
                while stack and stack[-1].right == temp:
                    temp = stack.pop()
                    result.append(temp.data)  # process the element
            else:
                curr = temp
    return result


def diameter(root: TreeNode) -> int:

    res = 0

    def dfs(root):
        nonlocal res

        if not root:
            return -1
        
        left = dfs(root.left)
        right = dfs(root.right)

        res = max(res, 2 + left + right)

        return 1 + max(left, right)
    
    dfs(root)

    return res
        

if __name__ == '__main__':
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
    # result = preorder_iterative(root)
    # print(result)
    # result = inorder_iterative(root)
    # print(result)
    # result = postorder_iterative(root)
    # print(result)

    d = diameter(root)
    print(d)



