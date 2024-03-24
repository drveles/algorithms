# Напишите программу для определения общего количества различных слов в строке текста.

def main():
    inputed = list(input().lower().split())

    for id in range(len(inputed)):
        inputed[id] = inputed[id].strip(" .,;:-?!")

    print(len(set(inputed)))


if __name__ == "__main__":
    main()
