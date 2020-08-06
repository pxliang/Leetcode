class Solution:
    def trap(self, height: List[int]) -> int:

        start = 0
        total = 0

        while start < len(height) - 1:
            temp = 0
            max_num = 0
            temp_num = 0
            point = start

            for end in range(start + 1, len(height)):
                if height[end] >= max_num:
                    max_num = height[end]
                    point = end
                    temp_num = temp

                    if height[end] >= height[start]:
                        break
                temp += height[end]

            total += (point - start - 1) * min(height[start], height[point]) - temp_num
            start = point

        return total
