class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:

        stack = [root]
        val_stack = [(5001, -1)]
        max_diff = -1

        while stack:
            current = stack.pop()
            min_value, max_value = val_stack.pop()
            if max_value >= 0:
                if abs(current.val - min_value) > max_diff:
                    max_diff = abs(current.val - min_value)
                if abs(current.val - max_value) > max_diff:
                    max_diff = abs(current.val - max_value)

            if current.left:
                stack.append(current.left)
                val_stack.append((min(current.val, min_value), max(current.val, max_value)))
            if current.right:
                stack.append(current.right)
                val_stack.append((min(current.val, min_value), max(current.val, max_value)))

        return max_diff

'''
1. the difference between ancestor and a node can be converted to the difference between descedant and a node
'''