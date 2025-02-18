def main():
    set1 = set(map(int, input().split()))
    set2 = set(map(int, input().split()))
    set3 = set(map(int, input().split()))

    print(*sorted((set1 | set2 | set3) - (set1 & set2 & set3)))

if __name__ == "__main__":
    main()