def main():
    info = {"name": "Ruslan", "age": 28, "name": "Timur"}

    unpack = [*info]

    print(info["name"])
    print(*info)
    print(unpack)
    print(info)

    capitals = {
        "Россия": "Москва",
        "Англия": "Лондон",
        "Чехия": "Прага",
        "Бразилия": "Бразилиа",
    }

    # сортировка по ключам
    for key in sorted(capitals):
        print(key)

    # сортировка по значениям
    for key, value in sorted(capitals.items(), key=lambda x: x[1]):
        print(value)


if __name__ == "__main__":
    main()
