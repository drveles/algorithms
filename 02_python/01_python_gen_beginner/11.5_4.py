numbers = [1, 2, 3, 4, 5]

def square(number):
    return number * number

squared_numbers_iterator = list(map(square, numbers))

print(squared_numbers_iterator)  # Выведет: [1, 4, 9, 16, 25]
