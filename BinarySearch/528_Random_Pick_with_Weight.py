class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        total = 0
        look = []
        for t, i in enumerate(self.w):
            total += i
            look.append(total)
        self.total = total
        self.look = look

    def pickIndex(self) -> int:

        num = random.randint(1, self.total)
        for t, n in enumerate(self.look):
            if n >= num:
                return t
