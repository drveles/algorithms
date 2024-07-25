week1 = input().split()
week2 = input().split()
week3 = input().split()
week4 = input().split()
days = {
    "MON": 0,
    "TUE": 1,
    "WED": 2,
    "THU": 3,
    "FRI": 4,
    "SAT": 5,
    "SUN": 6,
}
months = [[0] * 7 for i in range(4)]

for day in week1:
    months[0][days[day]] = 1
for day in week2:
    months[1][days[day]] = 1
for day in week3:
    months[2][days[day]] = 1
for day in week4:
    months[3][days[day]] = 1


temp_left = temp_right = left = 0
prev = True

days = []
for month in months:
    days.extend(month)

for right in range(28):
    if days[right]:
        temp_left = left if right - left > temp_right - temp_left else temp_left
        temp_right = right if right - left > temp_right - temp_left else temp_right
        prev = True
    if not days[right]:
        if prev:
            left = right
        prev = False
temp_left = left + 1 if right - left > temp_right - temp_left else temp_left + 1
temp_right = right + 1  if right - left > temp_right - temp_left else temp_right

if  sum(days) == 28:
    temp_left = 0
    temp_right = 0
if sum(days) == 0:
    temp_left = 1
    temp_right = 28

print(1 if sum(days) == 0 else temp_left, temp_right)
