_ = input()
shells = list(map(int, input().split()))
even = True  # четное

for shell in shells:
    temp = shell % 2
    if temp and not even:
        even = True
    elif temp and even:
        even = False

print("YES" if even else "NO")


print(filter(lambda x: x > 0, shells))
print(list(filter(lambda x: x > 0, shells)))

from functools import reduce

print(reduce(lambda x, y: x + y, shells))
print(reduce(lambda x, y: x + y, filter(lambda x: x > 0, shells)))
print(shells)
