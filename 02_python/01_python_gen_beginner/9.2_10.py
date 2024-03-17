# Программа должна вывести «YES», если слово является палиндромом, и «NO» в противном случае.
string = input()

flag = True
for i in range(len(string)):
    if string[i] != string[-(i + 1)]:
        flag = False
if flag:
    print("YES")
else:
    print("NO")
