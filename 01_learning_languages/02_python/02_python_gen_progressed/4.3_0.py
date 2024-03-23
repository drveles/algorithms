row = 3
col = 5
my_list = [[0] * col for _ in range(row)]
print(*my_list, sep='\n')