class RecentCounter:
    def __init__(self):
        self.array = []

    def ping(self, t: int) -> int:
        self.array.append(t)
        return len(self.array) - bisect_left(self.array, t - 3000)
