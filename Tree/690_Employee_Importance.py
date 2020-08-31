from collections import defaultdict

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        employ = defaultdict(list)
        value = defaultdict(int)

        for atr in employees:
            if atr.subordinates:
                employ[atr.id].extend(atr.subordinates)
            value[atr.id] = atr.importance

        stack = []
        importance = value[id]
        for n in employ[id]:
            stack.append(n)

        while stack:
            cur = stack.pop(0)
            importance += value[cur]
            for n in employ[cur]:
                stack.append(n)

        return importance