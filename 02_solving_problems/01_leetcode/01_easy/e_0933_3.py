class RecentCounter:
    def __init__(self):
        self.dual_queue = deque()

    def ping(self, t: int) -> int:
        self.dual_queue.append(t)
        left = self.dual_queue[0]
        while left < t - 3000:
            self.dual_queue.popleft()
            left = self.dual_queue[0]
        return len(self.dual_queue)
