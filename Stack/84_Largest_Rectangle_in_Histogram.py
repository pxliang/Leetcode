class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        if not heights:
            return 0

        stack = [[heights[0], 1]]
        result = 0
        for i in heights[1:]:
            if i > stack[-1][0]:
                stack.append((i, 1))
            elif i == stack[-1]:
                stack[-1][1] += 1
            else:
                val, time = stack.pop()
                pre = val * time
                width = time
                while stack and stack[-1][0] >= i:
                    val, time = stack.pop()
                    width += time
                    pre = max(pre, val * width)

                stack.append([i, width + 1])
                result = max(result, pre)

        val, time = stack.pop()
        pre = val * time
        width = time
        while stack:
            val, time = stack.pop()
            width += time
            pre = max(pre, val * width)

        return max(result, pre)