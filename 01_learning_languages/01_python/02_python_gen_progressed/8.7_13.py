def main():
    set1 = set(map(int, input().split()))
    set2 = set(map(int, input().split()))
    set3 = set(map(int, input().split()))
    set_all = set(range(11))

    print(*sorted(set_all - (set1 | set2 | set3)))

if __name__ == "__main__":
    main()