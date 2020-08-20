# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0

        def visit(root):
            if not root.left and not root.right:
                root.select = root.val
                root.noselect = 0
                return root

            if root.left:
                visit(root.left)
                no_left = root.left.noselect
                yes_left = root.left.select
            else:
                no_left = 0
                yes_left = 0

            if root.right:
                visit(root.right)
                no_right = root.right.noselect
                yes_right = root.right.select
            else:
                no_right = 0
                yes_right = 0

            root.select = no_left + no_right + root.val
            root.noselect = max(yes_left, no_left) + max(yes_right, no_right)

        visit(root)
        return max(root.noselect, root.select)

'''
comments:
1. Understand questions correctly: two connected nodes cannot be selected at the same time, but it doesn't mean
that parent or children node must be selected;
2. Tree top down or bottom up. In this question, if we use top down method, there are too many cases should be considered.
But if we review it from bottom up (sub-problem to the problem), the problem is broken down.
3. For the recursive method, the duplicate calculation is caused by multiple call of the same sub-problem. So if we can 
record the value down, we only need to look up the table to do it.
4. How to record the value during the bottom to up traverse process? We can use DFS (in a recursive way) to traverse the
node, and once we traverse the node, we change its attribute.  
'''