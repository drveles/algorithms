def main():
    people_counter = int(input())
    result_set = set(input())

    for _ in range(people_counter-1):
        result_set &= set(input())
    
    print(*sorted(list(result_set)))

if __name__ == "__main__":
    main()

#OK