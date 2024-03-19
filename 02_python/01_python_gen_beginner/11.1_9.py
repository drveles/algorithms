# Напишите программу, которая выводит список, состоящий из n букв английского алфавита

n = int(input())
array = []

for i in range(n):
    array.append(chr(97 + i))
print(array)