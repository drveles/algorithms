# Sample Input 4:
# 1   2  3   0
# 0   1  2  [3]
# -4 -3 -2  -1
# Sample Output 4:
# [[], ['1'], ['2'], ['3'], ['0'], ['1', '2'], ['2', '3'], ['3', '0'], ['1', '2', '3'], ['2', '3', '0'], ['1', '2', '3', '0']]

stock_list = list(map(int, input().split()))
len_list = len(stock_list)
result_list = [[]]

for dept in range(len_list - 1 ):
    temp_list = []  
    for len in range((len_list - dept - 1), -1, -1):
        for i in range(len+ 1):
            temp_list.append(stock_list[i:dept + i + 1])
        else:
            break
    result_list.extend(temp_list)
result_list.append(stock_list)

print(result_list)