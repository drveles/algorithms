# Напишите программу, которая по номеру курса выводит информацию о данном курсе.


def main():
    courses = {
        "CS101": ["3004,", "Хайнс,", "8:00"],
        "CS102": ["4501,", "Альварадо,", "9:00"],
        "CS103": ["6755,", "Рич,", "10:00"],
        "NT110": ["1244,", "Берк,", "11:00"],
        "CM241": ["1411,", "Ли,", "13:00"],
    }
    input_str = input()

    print(input_str + ":", *courses[input_str])


if __name__ == "__main__":
    main()
