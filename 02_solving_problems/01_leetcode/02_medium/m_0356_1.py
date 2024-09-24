# Даны координаты вида x1,y1 и x2, y2
# определить, можно ли провести паралельную прямую,
# которая бы делила расстояние между ними пополам?

# вопрос: есть ли какие-нибудь ограничения?

# Я думаю, что нужно проверить что у нас вопервых есть корректные пары по Y.
# тоесть, проверить, что у Y1 есть Y2 точка.
# можно собрать словарь точек Y c суммами всех точек по X
# перебрать весь словарь, убедившись, что у всех точек Y одинаковая середина


# def isReflected(nodes_left, nodes_right) -> bool:
#     y_dict = {}

#     for x1, y1 in nodes_left:
#         if y1 in y_dict:
#             y_dict[y1][0] += x1
#         else:
#             y_dict[y1] = [x1, 0]

#     for x1, y1 in nodes_right:
#         if y1 in y_dict:
#             y_dict[y1][1] += x1
#         else:
#             y_dict[y1] = [0, x1]

#     temp_middle = None

#     for x_list in y_dict.values():
#         temp_value = (x_list[0] + x_list[1]) / 2

#         if temp_middle is None:
#             temp_middle = temp_value
#         if temp_value != temp_middle:
#             return False

#     return True


# я не правильно понял задачу. Дано n точек в рандомный местах, нужно найти есть ли между ними линия

def isReflected(points: list[list[int]]) -> bool:
    max_x, min_x = float("-inf"), float("inf")
    unique_points = set()

    for x, y in points:
        max_x, min_x = max(max_x, x), min(min_x, x)
        unique_points.add((x, y,))
    
    summ_x = max_x + min_x

    for x, y in unique_points:
        if not (summ_x - x, y) in unique_points:
            return False
    
    return True



if __name__ == "__main__":
    points = [[1, 1], [-1, 1], [2, 3], [-2, 3], [0, 5]]
    # Ожидаемый результат: True
    # Пояснение: Существует линия x = 0, которая симметрична для всех точек.
    print(isReflected(points))
    points = [[1, 1], [-1, 1], [3, 2], [-2, 2], [0, 5]]
    print(isReflected(points))
    # Ожидаемый результат: False
    # Пояснение: Точка [3, 2] не имеет симметричной точки относительно линии.
    points = [[2, 1], [2, 3], [2, 5], [2, 7]]
    print(isReflected(points))
    # Ожидаемый результат: True
    # Пояснение: Все точки уже находятся на линии x = 2, линия симметрии совпадает с ними.
    points = [[1, 2], [-1, 2], [3, 4], [-3, 4], [5, 6], [-5, 6]]
    print(isReflected(points))
    # Ожидаемый результат: True
    # Пояснение: Линия симметрии x = 0 для всех точек.
    points = [[3, 5], [-3, 5], [6, 2], [-6, 2], [4, 1], [-4, 1], [2, 0], [-2, 0]]
    print(isReflected(points))
    # Ожидаемый результат: True
    # Пояснение: Линия симметрии находится на x = 0 для всех точек.
