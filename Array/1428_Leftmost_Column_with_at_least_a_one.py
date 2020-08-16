class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:

        row, col = binaryMatrix.dimensions()
        min_index = 10001
        for i in range(row):
            left = 0
            right = col - 1
            while left <= right:
                mid = (left + right) // 2
                if binaryMatrix.get(i, mid):
                    right = mid - 1
                else:
                    left = mid + 1

            if left < col:
                min_index = min(min_index, left)

        if min_index > 1000:
            return -1
        else:
            return min_index

### move left or down

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:

        row, col = binaryMatrix.dimensions()
        j = col - 1
        flag = 0
        for i in range(row):
            while j > -1 and binaryMatrix.get(i, j):
                j -= 1
                flag = 1

        if flag:
            return j + 1
        else:
            return -1

'''
comments:
1. not all rows need to be traversed
2. 
'''