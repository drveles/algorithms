def main():
    password_length = int(input())
    
    MOD = 10**9 + 7
    
    dp = [[0] * 4 for _ in range(password_length + 1)]
    
    dp[1][0] = 10
    dp[1][1] = 20
    dp[1][2] = 1
    dp[1][3] = 0
    
    for i in range(2, password_length + 1):
        dp[i][0] = ((dp[i-1][1] + dp[i-1][2] + dp[i-1][3]) * 10) % MOD
        dp[i][1] = (dp[i-1][0] * 20) % MOD
        dp[i][2] = (dp[i-1][0] * 1) % MOD
        dp[i][3] = (dp[i-1][1] * 2) % MOD
    
    total_natural_passwords = (dp[password_length][0] + dp[password_length][1] + 
                               dp[password_length][2] + dp[password_length][3]) % MOD
    
    print(total_natural_passwords)

if __name__ == "__main__":
    main()
