# Программа должна вывести одно число – количество пар элементов, равных друг другу.

splited_string = input().split()
counter = 0

for id1 in range(len(splited_string)):
    for id2 in range(id1 + 1, len(splited_string)):
        if splited_string[id1] == splited_string[id2]:
            counter += 1

print(counter)