### original solution
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

### dynamic solution

class Solution:
    def trap(self, height: List[int]) -> int:

        left_most = [0 for i in range(len(height))]
        right_most = [0 for i in range(len(height))]
        left_max = 0
        right_max = 0
        for i in range(len(height)):
            if height[i] > left_max:
                left_max = height[i]
            left_most[i] = left_max

            if height[len(height) - i - 1] > right_max:
                right_max = height[len(height) - i - 1]
            right_most[len(height) - i - 1] = right_max

        total = 0
        for i in range(len(height)):
            total += min(left_most[i], right_most[i]) - height[i]

        return total

'''
Comments:
1. right_most and left_most should include the current element, otherwise, it should consider the negative value
when calculate the total:
total += max(min(left_most[i], right_most[i]) - height[i], 0)
'''

### stack solution

class Solution:
    def trap(self, height: List[int]) -> int:

        stack = []
        total = 0
        top = 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = height[stack.pop()]
                if len(stack) == 0:
                    break
                distance = i - stack[-1] - 1
                total += distance * (min(height[i], height[stack[-1]]) - top)

            stack.append(i)

'''
comments:
1. think about the idea clearly: difference among three heights, and once a height is pop, its height should be 
subtracted in the following sum
'''
