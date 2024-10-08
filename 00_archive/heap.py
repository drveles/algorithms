import heapq

arr = [10,1,2,3,4]
heapq.heapify(arr)
print(type(arr))
print(arr)
print(heapq.heappop(arr))
print(heapq.heappop(arr))
print(heapq.heappop(arr))
print(heapq.heappop(arr))
print(heapq.heappop(arr))