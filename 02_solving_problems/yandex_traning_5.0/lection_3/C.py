# Дан массив a из n чисел.
# Найдите минимальное количество чисел, после удаления которых попарная разность оставшихся чисел по модулю не будет превышать 1,
# то есть после удаления ни одно число не должно отличаться от какого-либо другого более чем на 1.


def main():
    n = int(input())
    my_tuple = tuple(map(int, input().split()))

    couter_for_del = 0
    my_dict = {}
    most_used_el = min(my_tuple)

    for el in my_tuple:
        if el in my_dict:
            my_dict[el] += 1
        else:
            my_dict[el] = 1

    for el1 in my_dict:
        if el1 + 1 in my_dict:
            if most_used_el + 1 in my_dict:
                if (
                    my_dict[el1] + my_dict[el1 + 1]
                    >= my_dict[most_used_el] + my_dict[most_used_el + 1]
                ):
                    most_used_el = el1
            else:
                if my_dict[el1] + my_dict[el1 + 1] >= my_dict[most_used_el]:
                    most_used_el = el1

    for el2 in my_dict:
        if el2 != most_used_el and el2 != most_used_el + 1:
            couter_for_del += my_dict[el2]

    print(couter_for_del)


if __name__ == "__main__":
    main()

# OK