numbers = [34, 10, 4, 6, 10, 2]

result = {i: [k for k in [j for j in range(1, i + 1) if i // j == i / j]] for i in numbers }

print(result)