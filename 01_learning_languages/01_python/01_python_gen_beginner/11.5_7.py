seq = input().split('.')

for el in seq:
    if not(0 <= int(el) <= 255):
        print("НЕТ")
        break
else:
    print("ДА")