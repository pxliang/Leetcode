# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:

        result = []

        stack = [(root, 1)]
        while stack:
            cur, add = stack.pop()
            if cur.val in to_delete:
                add = 1
            else:
                if add:
                    result.append(cur)
                    add = 0

            if cur.left:
                stack.append((cur.left, add))
                if cur.left.val in to_delete:
                    cur.left = None
            if cur.right:
                stack.append((cur.right, add))
                if cur.right.val in to_delete:
                    cur.right = None

        return result



###recursive

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:

        result = []

        def Process(root):
            if not root:
                return None
            if root.val in to_delete:
                node_l = Process(root.left)
                if node_l:
                    result.append(node_l)
                node_r = Process(root.right)
                if node_r:
                    result.append(node_r)
                return None
            else:
                if not Process(root.left):
                    root.left = None
                if not Process(root.right):
                    root.right = None
                return root

        node = Process(root)
        if node:
            result.append(node)
        return result

'''
comments:
1. delete a node, need to let its parent know
'''