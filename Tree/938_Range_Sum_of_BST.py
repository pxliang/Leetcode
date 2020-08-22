class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:

        stack = [root]
        total = 0

        while stack:
            cur = stack.pop()
            if cur.val <= R and cur.val >= L:
                total += cur.val

            if cur.val > L and cur.left:
                stack.append(cur.left)

            if cur.val < R and cur.right:
                stack.append(cur.right)

        return total