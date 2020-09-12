# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:

        def Check(node1, node2):
            if not node1 and not node2:
                return True
            elif not node1:
                return False
            elif not node2:
                return False
            elif node1.val != node2.val:
                return False
            else:
                return (Check(node1.left, node2.left) and Check(node1.right, node2.right)) \
                       or (Check(node1.left, node2.right) and Check(node1.right, node2.left))

        return Check(root1, root2)


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