# Sample Input:
# 3
# 11helpme11jim11
# avengers141414atta11ck
# k1lg0re11111l

# Sample Output:
# 1

n = int(input())
counter = 0

for _ in range(n):
    string = input()

    if string.count("11") >= 3:
        counter += 1

print(counter)
