def main():
    people_counter = int(input())
    input() 
    result_set = set(input().split())

    for _ in range(people_counter-1):
        input()
        result_set &= set(input().split())
    
    print(len(result_set))
    print(*sorted(list(result_set)))

if __name__ == "__main__":
    main()

#OK