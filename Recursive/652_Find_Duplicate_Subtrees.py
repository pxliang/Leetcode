from collections import defaultdict


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:

        count = defaultdict(int)
        ans = set()

        def Serial(root):
            if not root:
                return '#'
            string = '{a},{b},{c}'.format(a=root.val, b=Serial(root.left), c=Serial(root.right))
            count[string] += 1
            if count[string] == 2:
                ans.add(root)

            return string

        string = Serial(root)
        return ans
