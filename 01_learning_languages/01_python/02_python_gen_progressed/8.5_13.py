#На вход программе подается строка текста, содержащая числа. 
# Для каждого числа выведите слово YES (в отдельной строке), 
# если это число ранее встречалось в последовательности или NO, если не встречалось.

def main():
    inputed = list(map(int, input().split()))
    inputed_set = set()

    for e in inputed:
        if e in inputed_set:
            print("YES")
        else:
            print("NO")
        inputed_set.add(e)


if __name__ == "__main__":
    main()
