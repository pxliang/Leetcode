from collections import defaultdict, deque


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        tree = defaultdict(list)
        for i, num in enumerate(manager):
            tree[num].append(i)

        queue = deque([(headID, 0)])
        inform = 0

        while queue:
            node, level = queue.popleft()
            if not node in tree:
                inform = max(inform, level)
            else:
                for i in tree[node]:
                    queue.append((i, level + informTime[node]))

        return inform
