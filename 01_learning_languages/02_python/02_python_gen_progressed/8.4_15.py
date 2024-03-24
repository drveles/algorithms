# На вход программе подаются две строки, состоящие из цифр. Необходимо определить, верно ли, что для записи этих строк были использованы одинаковые наборы цифр?

first_str_set = set(input())
second_str_set = set(input())

print("YES" if first_str_set == second_str_set else "NO")