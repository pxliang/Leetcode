from collections import defaultdict


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        if not matrix:
            return 0

        degree = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        graph = defaultdict(list)
        visit = set()
        stack = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i - 1 >= 0 and matrix[i - 1][j] > matrix[i][j]:
                    degree[i - 1][j] += 1
                    graph[(i, j)].append((i - 1, j))
                if j - 1 >= 0 and matrix[i][j - 1] > matrix[i][j]:
                    degree[i][j - 1] += 1
                    graph[(i, j)].append((i, j - 1))
                if j + 1 < len(matrix[0]) and matrix[i][j + 1] > matrix[i][j]:
                    degree[i][j + 1] += 1
                    graph[(i, j)].append((i, j + 1))
                if i + 1 < len(matrix) and matrix[i + 1][j] > matrix[i][j]:
                    degree[i + 1][j] += 1
                    graph[(i, j)].append((i + 1, j))

        for i in range(len(degree)):
            for j in range((len(degree[i]))):
                if degree[i][j] == 0:
                    stack.append((i, j))
                    visit.add((i, j))
        result = 0
        while stack:
            temp = []
            while stack:
                i, j = stack.pop()
                for edge in graph[(i, j)]:
                    degree[edge[0]][edge[1]] -= 1
                    if degree[edge[0]][edge[1]] == 0 and (not edge in visit):
                        temp.append(edge)
                        visit.add((edge))
            stack = temp
            result += 1

        return result