class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def euclid(x):
            return math.sqrt(x[0] ** 2 + x[1] ** 2)

        heap = []

        for point in points:
            heapq.heappush(heap, (euclid(point), point))
        
        return [heapq.heappop(heap)[1] for _ in range(k)]

#OK 56%, 92%