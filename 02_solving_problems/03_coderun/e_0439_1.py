# OK
import sys


def main():
    """
    Хочу пройтись по строке окном и посчитать их в словаре.
    Обойти словарь вручную и достать максимальное количество раз 
    и учесть максимальное в лексиграфическом порядке.
    """
    inp_string = input().strip()
    left = right = 0
    counter = {}
    result = ""

    while right < len(inp_string):
        if right - left < 1:
            right += 1
        elif inp_string[right] == " ":
            right += 1
            left = right
        else:
            counter[inp_string[left : right + 1]] = (
                counter.get(inp_string[left : right + 1], 0) + 1
            )
            left += 1
            right += 1

    for el in counter:
        if (
            counter[el] > counter.get(result, 0)
            or counter[el] == counter.get(result, 0)
            and el > result
        ):
            result = el

    print(result)


if __name__ == "__main__":
    main()
