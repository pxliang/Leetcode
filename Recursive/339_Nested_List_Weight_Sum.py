class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:

        def FindElement(nested, layer):

            total = 0
            for i in nested:
                if i.isInteger():
                    total += i.getInteger() * layer
                else:
                    total += FindElement(i.getList(), layer + 1)

            return total

        return FindElement(nestedList, 1)

'''
commnets:
1. the list of nested 
'''