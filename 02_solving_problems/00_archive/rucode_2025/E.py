def main():
    num_variables, num_equations = map(int, input().split())
    
    if num_equations > num_variables * (num_variables - 1) // 2:
        print(-1)
        return
    
    if num_equations >= num_variables - 1:
        min_diversity = 1
    else:
        min_diversity = num_variables - num_equations
    
    k = 1
    while k * (k - 1) // 2 < num_equations:
        k += 1
    max_diversity = num_variables - k + 1
    
    print(min_diversity, max_diversity)

if __name__ == "__main__":
    main()
