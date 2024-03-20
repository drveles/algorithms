# объявление функции
def merge(list1, list2):
    result = list1 + list2
    return sorted(result)

# считываем данные
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

# вызываем функцию
print(merge(numbers1, numbers2))