## Original solution

class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:

        result = []
        for i in range(len(A)):
            res_temp = []
            for j in range(len(B[0])):
                temp = 0
                for k in range(len(B)):
                    temp += A[i][k] * B[k][j]
                res_temp.append(temp)
            result.append(res_temp)

        return result

## check if the element is 0

class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:

        result = [[0 for i in range(len(B[0]))] for j in range(len(A))]
        for i in range(len(A)):
            for k in range(len(B)):
                if A[i][k]:
                    for j in range(len(B[0])):
                        result[i][j] += A[i][k] * B[k][j]

        return result

'''
Comments:
1. for loop can change
2. after changing the for loop sequence, check the result matrix
'''

## Record non-zero elements

class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:

        index = []
        for i in range(len(A)):
            temp = []
            for j in range(len(A[0])):
                if A[i][j]:
                    temp.append((j, A[i][j]))

            index.append(temp)

        result = [[0 for i in range(len(B[0]))] for j in range(len(A))]
        for i in range(len(index)):
            for j, num in index[i]:
                for k in range(len(B[0])):
                    result[i][k] += num * B[j][k]

        return result