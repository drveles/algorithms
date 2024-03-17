str = input()
counter = 0
for i in range(1, len(str)):
    if str[i] == str[i-1]:
        counter += 1
print(counter)