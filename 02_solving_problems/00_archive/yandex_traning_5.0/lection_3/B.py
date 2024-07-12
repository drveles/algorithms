# Выведите "YES" если одна из строк является анаграммой другой и "NO" в противном случае.

def main():
    str_1 = input()
    str_2 = input()
    set_1 = dict().fromkeys(str_1, 0)
    set_2 = dict().fromkeys(str_2, 0)

    for c in str_1:
        set_1[c] += 1
    for c in str_2:
        set_2[c] += 1
    
    print("YES" if set_1 == set_2 else "NO")

if __name__ == "__main__":
    main()

# OK