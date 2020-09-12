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
