# На вход программе подается строка текста, содержащая различные натуральные числа. 
# Из данной строки формируется список чисел. Напишите программу, которая меняет местами минимальный и максимальный элемент этого списка.

# Формат входных данных
# На вход программе подается строка текста, содержащая различные натуральные числа, разделенные символом пробела.

numbers = list(map(int, input().split())) 
index_min = numbers.index(min(numbers))
index_max = numbers.index(max(numbers))

numbers[index_min], numbers[index_max] = numbers[index_max], numbers[index_min]

print(*numbers)