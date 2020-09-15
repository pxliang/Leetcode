class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        if not matrix:
            return 0

        record = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix[0])):
            record[0][i] = int(matrix[0][i])

        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if int(matrix[i][j]):
                    record[i][j] = record[i - 1][j] + int(matrix[i][j])
                else:
                    record[i][j] = 0

        def Area(heights):

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

            # print(stack)
            val, time = stack.pop()
            pre = val * time
            width = time
            while stack:
                val, time = stack.pop()
                width += time
                pre = max(pre, val * width)

            return max(result, pre)

        max_num = 0
        for i in range(len(matrix)):
            max_num = max(Area(record[i]), max_num)

        return max_num