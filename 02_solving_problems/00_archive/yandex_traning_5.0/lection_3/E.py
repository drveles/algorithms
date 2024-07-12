# Вам даны три списка чисел. Найдите все числа, которые встречаются хотя бы в двух из трёх списков.

def main():
    input()
    set_1 = set(map(int, input().split()))
    input()
    set_2 = set(map(int, input().split()))
    input()
    set_3 = set(map(int, input().split()))

    print(*sorted(set_1 & set_2 | set_2 & set_3 | set_1 & set_3))

if __name__ == "__main__":
    main()

# OK