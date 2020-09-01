class MyCalendar:

    def __init__(self):
        self.queue = []

    def book(self, start: int, end: int) -> bool:
        if not self.queue:
            self.queue.append([start, end])
            return True
        if start < self.queue[0][0]:
            if end <= self.queue[0][0]:
                self.queue[0:0] = [[start, end]]
                return True
            else:
                return False
        else:
            start_l, start_r = 0, len(self.queue) - 1
            while start_l <= start_r:
                middle = (start_l + start_r) // 2
                if self.queue[middle][0] == start:
                    return False
                elif self.queue[middle][0] > start:
                    start_r = middle - 1
                else:
                    start_l = middle + 1

        if self.queue[start_r][1] > start:
            return False
        if start_l < len(self.queue) and self.queue[start_l][0] < end:
            return False

        self.queue[start_l:start_l] = [[start, end]]

        return True


'''
comments:
1. pay attention to corner case: insert a number to the head or tail of a list, <= or <
'''