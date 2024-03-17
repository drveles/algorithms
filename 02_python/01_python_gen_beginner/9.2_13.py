string = input()

print(
    string[(len(string) // 2 + len(string) % 2) :]
    + string[: (len(string) // 2 + len(string) % 2)]
)

#OK