from typing import List, Optional

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
    # go L L L then shift pointer to R then again go L L L 
    # when reached the right end keep on popping till the node is the R child
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


def postorder_iterative_simpler(root: TreeNode) -> List:
    # almost similar to preorder but the parent node 
    # is only popped when being visited the second time
    stack = []
    res = []
    stack.append((root, False))  # False mean not yet visited
    
    while stack:
        node, v = stack.pop()
        if v:
            res.append(node.data)
        else:
            stack.append((node, True))
            if node.right: stack.append((node.right, False))
            if node.left: stack.append((node.left, False))
    
    return res
        


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
        


def all_root_to_leaf_paths(root: TreeNode) -> List[List]:
    
    res = []
    if not root:
        return res

    def helper(root, prev_path):
        if not root.left and not root.right:
            prev_path.append(root.data)
            res.append(prev_path[:])
            return
        
        prev_path.append(root.data)
        if root.left: helper(root.left, prev_path[:])
        if root.right: helper(root.right, prev_path[:])

    helper(root, [])

    return res


def sum_of_all_root_to_left_paths(root: TreeNode) -> int:
    # given each path represents a number 1->2->3 == 123

    res = 0
    def dfs(node, prevSum):
        nonlocal res

        if not node:
            return
        
        currSum = 10 * prevSum + node.data

        if not node.left and not node.right:
            res += currSum
            return
        
        dfs(node.left, currSum)
        dfs(node.right, currSum)

    dfs(root, 0)
    return res


def max_path_sum_bw_any_two_nodes(root: TreeNode) -> int:
    res = 0

    def dfs(node) -> int:
        nonlocal res
        if not node:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        res = max(res, node.data + (0 if left < 0 else left) + (0 if right < 0 else right))
        return node.data + max(0, left, right)

    dfs(root)

    return res


def lca(root: TreeNode, alpha: TreeNode, beta: TreeNode) -> Optional[TreeNode]:
    if not root:
        return root

    if root.data == alpha.data or root.data == beta.data:
        return root
    left = lca(root.left, alpha, beta)
    right = lca(root.right, alpha, beta)

    if left and right:
        return root
    
    return left if left else right


def all_ancestors(root, node):
    if not root:
        return
    
    if root == node:
        return True
    
    left = all_ancestors(root.left, node)
    right = all_ancestors(root.right, node)

    if left or right:
        print(root.data)
        return True


def column_sum(root):
    res = {}

    def dfs(node, col):
        if not node:
            return
        if col in res:
            res[col] += node.data
        else:
            res[col] = node.data

        dfs(node.left, col-1)
        dfs(node.right, col+1)
    
    dfs(root, 0)
    return res


def top_view(root):
    from collections import OrderedDict
    res = OrderedDict()

    def dfs(node, col):
        if not node:
            return
        if col not in res:
            res[col] = node
        
        dfs(node.left, col-1)
        dfs(node.right, col+1)

    dfs(root, 0)
    return res




if __name__ == '__main__':
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7, TreeNode(8), TreeNode(9))))
    # result = preorder_iterative(root)
    # print(result)
    # result = inorder_iterative(root)
    # print(result)
    # result = postorder_iterative(root)
    # print(result)

    # d = diameter(root)
    # print(d)

    # paths = all_root_to_leaf_paths(root)
    # print(paths)

    # res = sum_of_all_root_to_left_paths(root)
    # print(res)

    # res = max_path_sum_bw_any_two_nodes(root)
    # print(res)

    # print(lca(root, root.left, root.right))
    # print(lca(root, root.left.left, root.left.right))
    # print(lca(root, root.left.left, root.right.left))

    # all_ancestors(root, root.right.right)

    # res = column_sum(root)
    # for k, v in res.items():
    #     print(k, v)

    # res = top_view(root)
    # print(type(res))
    # for k, v in res.items():
    #     print(k, v)

    # res = postorder_iterative_simpler(root)
    # print(res)

