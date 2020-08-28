class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if (not self.stack) or (self.stack[-1] - self.stack[0] < 300):
            self.stack.append(timestamp)
        else:
            self.stack.pop(0)
            self.stack.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if (not self.stack) or (timestamp - self.stack[-1] >= 300):
            return 0
        if timestamp - self.stack[0] < 300:
            return len(self.stack)

        left = 0
        right = len(self.stack) - 1
        while left <= right:
            middle = (left + right) // 2
            if timestamp - self.stack[middle] >= 300:
                left = middle + 1
            else:
                right = middle - 1

        return len(self.stack[left:])