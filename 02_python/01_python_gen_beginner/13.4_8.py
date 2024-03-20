# объявление функции
def get_factors(num):
    result = [i for i in range(1, num + 1) if num % i == 0]
    return result

# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))