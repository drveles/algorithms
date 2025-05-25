"""
Даны координаты вида x1,y1 и x2, y2
определить, можно ли провести паралельную прямую,
которая бы делила расстояние между ними пополам?
"""


def isReflected(points: list[list[int]]) -> bool:
    max_x, min_x = float("-inf"), float("inf")
    unique_points = set()

    for x, y in points:
        max_x, min_x = max(max_x, x), min(min_x, x)
        unique_points.add((x, y))

    summ_x = max_x + min_x

    for x, y in unique_points:
        if not (summ_x - x, y) in unique_points:
            return False

    return True


if __name__ == "__main__":
    # Существует линия x = 0, которая симметрична для всех точек.
    points = [[1, 1], [-1, 1], [2, 3], [-2, 3], [0, 5]]
    assert isReflected(points) == True

   # Точка [3, 2] не имеет симметричной точки относительно линии.
    points = [[1, 1], [-1, 1], [3, 2], [-2, 2], [0, 5]]
    assert isReflected(points) == False

    # Ожидаемый результат: True
    points = [[2, 1], [2, 3], [2, 5], [2, 7]]
    assert isReflected(points) == True

    # Все точки уже находятся на линии x = 2, линия симметрии совпадает с ними.
    points = [[1, 2], [-1, 2], [3, 4], [-3, 4], [5, 6], [-5, 6]]
    assert isReflected(points) == True

    # Есть линия симметрии x = 0 для всех точек.
    points = [[3, 5], [-3, 5], [6, 2], [-6, 2], [4, 1], [-4, 1], [2, 0], [-2, 0]]
    assert isReflected(points) == True
