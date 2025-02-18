my_dict = {"apple": 5, "banana": 3, "orange": 2}

# Получение значения элемента по ключу
apple_count = my_dict.get("apple")
print(apple_count)  # Вывод: 5

# Получение значения элемента по несуществующему ключу
pear_count = my_dict.get("pear")
print(pear_count)  # Вывод: None

# Получение значения элемента по несуществующему ключу с указанием значения по умолчанию
pear_count = my_dict.get("pear", 0)
print(pear_count)  # Вывод: 0
print(my_dict)  # Вывод: 0