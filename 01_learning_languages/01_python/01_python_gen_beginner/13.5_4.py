# объявление функции
def is_prime(num):
    result = True
    if num == 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            result = False
            break

    return result


# объявление функции
def get_next_prime(num):
    flag = False

    while not flag:
        num += 1
        if is_prime(num):
            break

    return num


# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))