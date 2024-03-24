# Напишите программу для вывода количества уникальных символов каждого считанного слова без учета регистра.

def uniq_symb(inp_set):
    return(len(inp_set))

def main():
    n = int(input())
    for i in range(n):
        temp_set = set(input().lower())
        print(uniq_symb(temp_set))        

if __name__ == "__main__":
    main()
