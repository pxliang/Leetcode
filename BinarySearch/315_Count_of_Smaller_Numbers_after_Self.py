class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:

        if not nums:
            return None

        def Insert(val, binary):
            left = 0
            right = len(binary) - 1

            while left <= right:
                middle = (left + right) // 2
                if val > binary[middle]:
                    left = middle + 1
                else:
                    right = middle - 1

            binary.insert(left, val)
            return binary, left

        result = [0]
        binary = [nums[-1]]
        for i in nums[::-1][1:]:
            binary, count = Insert(i, binary)
            result.append(count)

        return result[::-1]