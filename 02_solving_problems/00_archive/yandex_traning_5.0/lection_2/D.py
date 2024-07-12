counter_squares = int(input())
field_list_list = [0] * 8
neighbourhoods = 0

for i in range(8):
    field_list_list[i] = [0] * 8  # type: ignore
for _ in range(counter_squares):
    i, j = map(int, input().split())
    field_list_list[i - 1][j - 1] = 1
for i in range(7):
    for j in range(7):
        if field_list_list[i][j] and field_list_list[i + 1][j]:
            neighbourhoods += 1
        if field_list_list[i][j] and field_list_list[i][j + 1]:
            neighbourhoods += 1
for i in range(7):
    if field_list_list[7][i] and field_list_list[7][i + 1]:
        neighbourhoods += 1
for i in range(7):
    if field_list_list[i][7] and field_list_list[i + 1][7]:
        neighbourhoods += 1

print(counter_squares * 4 - neighbourhoods * 2)

# OK