def main():
    set1 = set(input())
    set2 = set(input())

    print("YES" if set1.intersection(set2) else "NO")

if __name__ == "__main__":
    main()