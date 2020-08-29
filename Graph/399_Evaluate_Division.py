from collections import defaultdict


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = defaultdict(list)

        for i, string in enumerate(equations):
            a, b = string
            graph[a].append((b, values[i]))
            graph[b].append((a, 1 / values[i]))

        result = []
        for string in queries:
            a, b = string
            stack = []
            find = 0
            visit = set()
            for sub in graph[a]:
                stack.append(sub)
                visit.add(sub[0])
            while stack:
                cur_letter, cur_value = stack.pop()
                if cur_letter == b:
                    find = 1
                    result.append(cur_value)
                    break
                for sub in graph[cur_letter]:
                    if sub[0] not in visit:
                        stack.append((sub[0], cur_value * sub[1]))
                        visit.add(sub[0])
            if not find:
                result.append(-1.0)

        return result

'''
comments:
1.  in DFS, you should judge if a node is visited or not. Otherwise, it will stuck in the deadlock
'''