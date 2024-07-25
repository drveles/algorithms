_ = input()
shells = list(map(int, input().split()))
even = True # четное

for shell in shells: 
    temp = shell % 2
    if temp and not even:
        even = True
    elif temp and even:
        even = False

print("YES" if even else "NO")
